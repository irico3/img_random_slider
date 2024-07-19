import random
import sys

from PIL import Image


def main():
    print("🧩img random slider")

    try:
        args = sys.argv
        image_path: str = args[1]
        column: int = int(args[2])

        #  画像をランダムに分割する
        cellCount = column * column
        randomArray = [i for i in range(cellCount)]
        random.shuffle(randomArray)

        #  randomArrayに合わせて画像を加工する
        img = Image.open(image_path)
        dst = Image.new("RGB", (img.width, img.height))

        cellWidth = img.width // column
        cellHeight = img.height // column
        print(cellWidth, cellHeight)

        for distI, srcI in enumerate(randomArray):
            # 4(column) x 4(column) の場合 i が5の場合
            # targetRow = 1, targetColumn = 0
            targetRow = srcI // column
            targetColumn = srcI % column

            cell = img.crop(
                (
                    targetColumn * cellWidth,
                    targetRow * cellHeight,
                    (targetColumn + 1) * cellWidth,
                    (targetRow + 1) * cellHeight,
                )
            )

            distRow = distI // column
            distColumn = distI % column
            dst.paste(cell, (distRow * cellWidth, distColumn * cellHeight))

        dst.save("output.jpg")

    except Exception as e:
        print(f"please input the correct command. {e}")
        print("hint: python index.py [image path] [split column]")
        sys.exit()


main()
