---
layout: default
title: MFE-GAN: Efficient GAN-based Framework for Document Image Enhancement and Binarization with Multi-scale Feature Extraction
---

# MFE-GAN: Efficient GAN-based Framework for Document Image Enhancement and Binarization with Multi-scale Feature Extraction

**arXiv**: [2512.14114v1](https://arxiv.org/abs/2512.14114) | [PDF](https://arxiv.org/pdf/2512.14114.pdf)

**作者**: Rui-Yang Ju, KokSheik Wong, Yanlin Jin, Jen-Shiun Chiang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Extended Journal Version of APSIPA ASC 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://ruiyangju.github.io/MFE-GAN)

---

## 💡 一句话要点

**提出MFE-GAN框架，通过多尺度特征提取和Haar小波变换，高效解决文档图像增强与二值化问题。**

**关键词**: `文档图像增强` `图像二值化` `生成对抗网络` `多尺度特征提取` `Haar小波变换` `光学字符识别` `高效训练` `消融研究`

## 📋 核心要点

1. 现有方法使用多个独立GAN处理不同颜色通道，导致训练和推理时间过长，效率低下。
2. 提出MFE-GAN框架，结合Haar小波变换和多尺度特征提取，优化图像预处理，并设计新生成器、判别器和损失函数。
3. 实验显示，MFE-GAN在多个数据集上显著减少训练和推理时间，同时性能与SOTA方法相当。

## 📝 摘要（中文）

文档图像增强与二值化通常在文档分析与识别任务前执行，以提高光学字符识别（OCR）系统的效率和准确性。这是因为直接识别退化文档（特别是彩色图像）中的文本往往导致不理想的识别性能。为解决这些问题，现有方法训练独立的生成对抗网络（GANs）处理不同颜色通道以去除阴影和噪声，从而促进高效的文本信息提取。然而，部署多个GANs会导致训练和推理时间过长。为减少文档图像增强与二值化模型的训练和推理时间，我们提出了MFE-GAN，这是一种基于GAN的高效框架，采用多尺度特征提取（MFE），结合Haar小波变换（HWT）和归一化处理文档图像，然后输入GANs进行训练。此外，我们提出了新颖的生成器、判别器和损失函数以提升模型性能，并通过消融研究验证其有效性。在Benchmark、Nabuco和CMATERdb数据集上的实验结果表明，所提出的MFE-GAN显著减少了总训练和推理时间，同时保持了与最先进（SOTA）方法相当的性能。本工作的实现可在https://ruiyangju.github.io/MFE-GAN获取。

## 🔬 方法详解

MFE-GAN是一个基于生成对抗网络的高效框架，整体架构包括预处理模块和多尺度特征提取模块。关键技术创新点在于引入Haar小波变换和归一化进行图像预处理，以及设计新颖的生成器和判别器结构，结合多尺度特征提取来捕获文档图像的全局和局部信息。与现有方法的主要区别在于，它避免了使用多个独立GAN处理不同颜色通道，而是通过统一的框架和优化预处理步骤，显著降低了计算复杂度，提高了训练和推理效率。

## 📊 实验亮点

在Benchmark、Nabuco和CMATERdb数据集上的实验表明，MFE-GAN显著减少了总训练和推理时间，同时保持了与最先进方法相当的性能，验证了其高效性和有效性。

## 🎯 应用场景

该研究主要应用于文档图像处理领域，特别是在光学字符识别（OCR）系统中，用于增强退化文档图像（如去除阴影和噪声）并进行二值化，以提高文本识别的准确性和效率。潜在应用包括数字化档案管理、历史文档修复、移动设备扫描应用等，具有实际价值在于提升自动化文档处理的速度和可靠性。

## 📄 摘要（原文）

> Document image enhancement and binarization are commonly performed prior to document analysis and recognition tasks for improving the efficiency and accuracy of optical character recognition (OCR) systems. This is because directly recognizing text in degraded documents, particularly in color images, often results in unsatisfactory recognition performance. To address these issues, existing methods train independent generative adversarial networks (GANs) for different color channels to remove shadows and noise, which, in turn, facilitates efficient text information extraction. However, deploying multiple GANs results in long training and inference times. To reduce both training and inference times of document image enhancement and binarization models, we propose MFE-GAN, an efficient GAN-based framework with multi-scale feature extraction (MFE), which incorporates Haar wavelet transformation (HWT) and normalization to process document images before feeding them into GANs for training. In addition, we present novel generators, discriminators, and loss functions to improve the model's performance, and we conduct ablation studies to demonstrate their effectiveness. Experimental results on the Benchmark, Nabuco, and CMATERdb datasets demonstrate that the proposed MFE-GAN significantly reduces the total training and inference times while maintaining comparable performance with respect to state-of-the-art (SOTA) methods. The implementation of this work is available at https://ruiyangju.github.io/MFE-GAN.

