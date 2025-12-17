---
layout: default
title: Computer vision training dataset generation for robotic environments using Gaussian splatting
---

# Computer vision training dataset generation for robotic environments using Gaussian splatting

**arXiv**: [2512.13411v1](https://arxiv.org/abs/2512.13411) | [PDF](https://arxiv.org/pdf/2512.13411.pdf)

**作者**: Patryk Niżeniec, Marcin Iwanowski

---

## 💡 一句话要点

**提出基于高斯泼溅的机器人视觉数据集生成流水线，以解决合成与真实图像域差距和手动标注瓶颈。**

**关键词**: `高斯泼溅` `数据集生成` `机器人视觉` `合成数据` `域适应` `自动标注`

## 📋 核心要点

1. 核心问题：合成与真实图像域差距及手动标注耗时，阻碍机器人视觉数据集生成。
2. 方法要点：利用3D高斯泼溅创建逼真环境，结合游戏引擎物理模拟和两遍渲染增强真实感。
3. 实验或效果：混合少量真实图像与大量合成数据训练，提升检测与分割性能，验证为高效策略。

## 📄 摘要（原文）

> This paper introduces a novel pipeline for generating large-scale, highly realistic, and automatically labeled datasets for computer vision tasks in robotic environments. Our approach addresses the critical challenges of the domain gap between synthetic and real-world imagery and the time-consuming bottleneck of manual annotation. We leverage 3D Gaussian Splatting (3DGS) to create photorealistic representations of the operational environment and objects. These assets are then used in a game engine where physics simulations create natural arrangements. A novel, two-pass rendering technique combines the realism of splats with a shadow map generated from proxy meshes. This map is then algorithmically composited with the image to add both physically plausible shadows and subtle highlights, significantly enhancing realism. Pixel-perfect segmentation masks are generated automatically and formatted for direct use with object detection models like YOLO. Our experiments show that a hybrid training strategy, combining a small set of real images with a large volume of our synthetic data, yields the best detection and segmentation performance, confirming this as an optimal strategy for efficiently achieving robust and accurate models.

