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

**提出MFE-GAN框架，通过多尺度特征提取提升文档图像增强与二值化效率，减少训练和推理时间。**

🎯 **匹配领域**: **强化学习**

**关键词**: `文档图像增强` `图像二值化` `生成对抗网络` `多尺度特征提取` `哈尔小波变换` `光学字符识别` `高效训练` `模型优化`

## 📋 核心要点

1. 现有方法使用多个独立GAN处理不同颜色通道，导致训练和推理时间过长，效率低下。
2. 提出MFE-GAN框架，集成多尺度特征提取（MFE）和哈尔小波变换，优化图像预处理和GAN架构。
3. 实验显示MFE-GAN在多个数据集上显著减少时间消耗，同时性能与SOTA方法相当，验证了其高效性。

## 📝 摘要（中文）

文档图像增强和二值化通常在文档分析与识别任务前执行，以提高光学字符识别（OCR）系统的效率和准确性。这是因为直接识别退化文档（尤其是彩色图像）中的文本往往导致不理想的识别性能。为解决这些问题，现有方法训练独立的生成对抗网络（GAN）处理不同颜色通道以去除阴影和噪声，从而促进高效的文本信息提取。然而，部署多个GAN会导致较长的训练和推理时间。为减少文档图像增强和二值化模型的训练和推理时间，我们提出了MFE-GAN，这是一种基于GAN的高效框架，采用多尺度特征提取（MFE），结合哈尔小波变换（HWT）和归一化处理文档图像，然后输入GAN进行训练。此外，我们提出了新颖的生成器、判别器和损失函数以提升模型性能，并通过消融研究验证其有效性。在Benchmark、Nabuco和CMATERdb数据集上的实验结果表明，所提出的MFE-GAN显著减少了总训练和推理时间，同时保持了与最先进（SOTA）方法相当的性能。本工作的实现可在https://ruiyangju.github.io/MFE-GAN获取。

## 🔬 方法详解

MFE-GAN是一个基于生成对抗网络（GAN）的高效框架，用于文档图像增强和二值化。整体框架包括多尺度特征提取（MFE）模块，该模块利用哈尔小波变换（HWT）和归一化对输入图像进行预处理，提取多尺度特征后输入到GAN中进行训练。关键技术创新点包括：新颖的生成器和判别器设计，以及优化的损失函数，这些改进提升了模型处理退化文档的能力。与现有方法的主要区别在于，MFE-GAN通过集成MFE模块避免了使用多个独立GAN，从而减少了模型复杂度和计算开销，实现了更快的训练和推理速度，同时保持了图像增强和二值化的质量。

## 📊 实验亮点

在Benchmark、Nabuco和CMATERdb数据集上的实验表明，MFE-GAN显著减少了总训练和推理时间，同时性能与最先进方法相当，消融研究验证了其新颖组件（如生成器、判别器和损失函数）的有效性，突出了框架的高效性和实用性。

## 🎯 应用场景

该研究主要应用于文档分析与识别领域，特别是光学字符识别（OCR）系统。通过高效增强和二值化退化文档图像，如去除阴影和噪声，可以提升OCR的准确性和效率，适用于数字化档案处理、历史文档修复、自动化办公等实际场景，具有重要的工业应用价值。

## 📄 摘要（原文）

> Document image enhancement and binarization are commonly performed prior to document analysis and recognition tasks for improving the efficiency and accuracy of optical character recognition (OCR) systems. This is because directly recognizing text in degraded documents, particularly in color images, often results in unsatisfactory recognition performance. To address these issues, existing methods train independent generative adversarial networks (GANs) for different color channels to remove shadows and noise, which, in turn, facilitates efficient text information extraction. However, deploying multiple GANs results in long training and inference times. To reduce both training and inference times of document image enhancement and binarization models, we propose MFE-GAN, an efficient GAN-based framework with multi-scale feature extraction (MFE), which incorporates Haar wavelet transformation (HWT) and normalization to process document images before feeding them into GANs for training. In addition, we present novel generators, discriminators, and loss functions to improve the model's performance, and we conduct ablation studies to demonstrate their effectiveness. Experimental results on the Benchmark, Nabuco, and CMATERdb datasets demonstrate that the proposed MFE-GAN significantly reduces the total training and inference times while maintaining comparable performance with respect to state-of-the-art (SOTA) methods. The implementation of this work is available at https://ruiyangju.github.io/MFE-GAN.

