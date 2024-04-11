import sys
import cv2
import numpy as np


class Verify_code:
    def __init__(self):
        try:
            self.image = cv2.imread("./verify.jpg")
        except Exception as e:
            print(e)
            sys.exit(0)

    def split_captcha_picture(self):
        little_img_list = []
        for x_index in range(3):
            for y_index in range(3):
                little_img_list.append(self.image[x_index * 100:(x_index + 1) * 100, y_index * 100:(y_index + 1) * 100])
        # cv2.imshow('xxx', little_img_list[5])
        # cv2.waitKey()
        return little_img_list

    def wipe_black(self, threshold):
        img_b = self.image[:, :, 0].copy()
        img_g = self.image[:, :, 1].copy()
        img_r = self.image[:, :, 2].copy()
        # colors = img_b*256*256 + img_g*256 + img_r  # 编码
        flag = (img_b <= threshold) | (img_g <= threshold) | (img_r <= threshold)
        img_b[flag] = 255
        img_g[flag] = 255
        img_r[flag] = 255
        self.image = cv2.merge((img_b, img_g, img_r))

    def process_captcha_picture(self):
        self.__show_image("verify")
        self.wipe_black(10)
        self.__show_image("wipe_black")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # self.__bgr2gray()
        self.__show_image("gray_img")
        # self.image = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        # self.__show_image("binary_img")

        # 腐蚀去漏洞
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.image = cv2.erode(self.image, kernel)
        self.__show_image("erode")
        # 膨胀拓展图像大小
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        self.image = cv2.dilate(self.image, kernel)
        self.__show_image("dilate")
        # 二值化
        max_color = np.argmax(np.bincount(np.ravel(self.image)))
        self.image[(self.image < max_color + 5) & (self.image > max_color - 5)] = 255
        self.image[self.image != 255] = 0
        self.__show_image("binary")
        self.__wipe_noise()
        self.__show_image("noise")
        return self.split_captcha_picture()

    def __show_image(self, name):
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __bgr2gray(self):
        h, w = self.image.shape[:2]
        result = np.zeros((h, w), np.uint8)
        for i in range(h):
            for j in range(w):
                result[i, j] = max(self.image[i, j][0], self.image[i, j][1], self.image[i, j][2])
        self.image = result

    def __wipe_noise(self):
        h, w = self.image.shape
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                count = 0
                if self.image[i - 1, j] == 255:
                    count += 1
                if self.image[i, j - 1] == 255:
                    count += 1
                if self.image[i, j + 1] == 255:
                    count += 1
                if self.image[i + 1, j] == 255:
                    count += 1
                if self.image[i + 1, j - 1] == 255:
                    count += 1
                if self.image[i + 1, j + 1] == 255:
                    count += 1
                if self.image[i - 1, j - 1] == 255:
                    count += 1
                if self.image[i - 1, j + 1] == 255:
                    count += 1
                if count > 4:
                    self.image[i, j] = 255
