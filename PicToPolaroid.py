from PIL import Image, ImageEnhance, ImageDraw, ImageFilter, ImageTk
from tkinter import Tk, Button, Label, filedialog, messagebox, Canvas
import os


class PolaroidApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Polaroid-ize Your Photo')

        self.imagePath = None
        self.image = None
        self.originalImage = None
        self.croppedImage = None
        self.canvas = None
        self.squareSize = 100
        self.square = None
        self.topLeft = (0, 0)
        self.maxSize = 500

        self.label = Label(root, text='Polaroid Effect Generator', font=('Arial', 14))
        self.label.pack(pady=10)

        self.chooseButton = Button(root, text='Choose Photo', command=self.openFileDialog)
        self.chooseButton.pack(pady=20)

        self.confirmButton = Button(root, text='Confirm Crop', command=self.confirmCrop)
        self.confirmButton.pack(pady=10)

        self.exitButton = Button(root, text='Exit', command=root.quit)
        self.exitButton.pack(pady=10)

    def openFileDialog(self):
        filepath = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg *.jpeg *.png')])
        if filepath:
            self.imagePath = filepath
            self.loadImage()

    def loadImage(self):
        self.originalImage = Image.open(self.imagePath)
        self.image = self.resizeImage(self.originalImage)

        self.tkImage = ImageTk.PhotoImage(self.image)

        if self.canvas:
            self.canvas.destroy()

        self.canvas = Canvas(self.root, width=self.tkImage.width(), height=self.tkImage.height())
        self.canvas.pack(pady=20)

        self.canvas.create_image(0, 0, anchor='nw', image=self.tkImage)

        self.squareSize = min(self.image.size)

        self.square = self.canvas.create_rectangle(self.topLeft[0], self.topLeft[1],
                                                   self.topLeft[0] + self.squareSize,
                                                   self.topLeft[1] + self.squareSize,
                                                   outline='red', width=2)

        self.canvas.bind('<B1-Motion>', self.moveSquare)

    def resizeImage(self, image):
        width, height = image.size
        aspectRatio = width / height

        if width > height:
            newWidth = self.maxSize
            newHeight = int(newWidth / aspectRatio)
        else:
            newHeight = self.maxSize
            newWidth = int(newHeight * aspectRatio)

        return image.resize((newWidth, newHeight))

    def moveSquare(self, event):
        x = event.x
        y = event.y

        x = max(0, min(x, self.image.width - self.squareSize))
        y = max(0, min(y, self.image.height - self.squareSize))

        self.canvas.coords(self.square, x, y, x + self.squareSize, y + self.squareSize)
        self.topLeft = (x, y)

    def confirmCrop(self):
        originalWidth, originalHeight = self.originalImage.size
        scaleX = originalWidth / self.image.width
        scaleY = originalHeight / self.image.height

        left = int(self.topLeft[0] * scaleX)
        top = int(self.topLeft[1] * scaleY)
        right = int((self.topLeft[0] + self.squareSize) * scaleX)
        bottom = int((self.topLeft[1] + self.squareSize) * scaleY)

        self.croppedImage = self.originalImage.crop((left, top, right, bottom))
        self.applyPolaroidEffects()

    def applyPolaroidEffects(self):
        try:
            polaroidImageTemp = self.polaroidEffects(self.croppedImage)
            polaroidImage = self.addPolaroidFrame(polaroidImageTemp)

            scriptDirectory = os.path.dirname(os.path.abspath(__file__))
            outputPath = os.path.join(scriptDirectory,'polaroidOutput.jpg')

            polaroidImage.save(outputPath)
            messagebox.showinfo('Success', f'Polaroid image saved as {outputPath}')
            print(f'Polaroid image saved as {outputPath}')
        except Exception as e:
            messagebox.showerror('Error', f'An error occurred: {e}')
            print(f'An error occurred: {e}')

    def polaroidEffects(self, image):
        brightness = ImageEnhance.Brightness(image)
        image = brightness.enhance(1.1)

        contrast = ImageEnhance.Contrast(image)
        image = contrast.enhance(0.85)

        saturation = ImageEnhance.Color(image)
        image = saturation.enhance(0.7)

        vignette = Image.new('L', image.size, 255)
        draw = ImageDraw.Draw(vignette)

        for i in range(4):
            xOffset = (i % 2) * (image.width - self.squareSize)
            yOffset = (i // 2) * (image.height - self.squareSize)
            draw.rectangle([xOffset, yOffset, xOffset + self.squareSize, yOffset + self.squareSize], fill=0)

        vignette = vignette.filter(ImageFilter.GaussianBlur(60))
        vignette.putalpha(120)
        image = Image.composite(image, Image.new('RGB', image.size, (0, 0, 0)), vignette)

        noise = Image.effect_noise(image.size, 10)
        image = Image.blend(image, noise.convert('RGB'), alpha=0.15)

        return image

    def addPolaroidFrame(self, image, frameColor=(255, 255, 255), sideBorderRatio=0.05, bottomBorderRatio=0.2):
        width, height = image.size
        sideBorderWidth = int(width * sideBorderRatio)
        bottomBorderWidth = int(height * bottomBorderRatio)

        polaroidWidth = width + sideBorderWidth * 2
        polaroidHeight = height + sideBorderWidth + bottomBorderWidth
        polaroidImage = Image.new('RGB', (polaroidWidth, polaroidHeight), frameColor)

        polaroidImage.paste(image, (sideBorderWidth, sideBorderWidth))
        return polaroidImage


root = Tk()
app = PolaroidApp(root)
root.mainloop()
