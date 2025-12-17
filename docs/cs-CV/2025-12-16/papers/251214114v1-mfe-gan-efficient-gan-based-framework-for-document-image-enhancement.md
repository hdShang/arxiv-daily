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

**提出MFE-GAN框架，通过多尺度特征提取和Haar小波变换，高效解决文档图像增强与二值化中的训练和推理时间问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `文档图像增强` `图像二值化` `生成对抗网络` `多尺度特征提取` `Haar小波变换` `光学字符识别` `高效训练` `消融研究`

## 📋 核心要点

1. 核心问题：现有方法使用多个独立GAN处理不同颜色通道，导致训练和推理时间过长，效率低下。
2. 方法要点：提出MFE-GAN框架，集成多尺度特征提取和Haar小波变换，优化图像预处理，减少模型复杂度。
3. 实验或效果：在多个数据集上验证，MFE-GAN显著降低时间成本，同时性能与SOTA方法相当。

## 📝 摘要（中文）

文档图像增强和二值化通常在文档分析和识别任务之前进行，以提高光学字符识别（OCR）系统的效率和准确性。这是因为直接识别退化文档（尤其是彩色图像）中的文本往往导致不理想的识别性能。为解决这些问题，现有方法训练独立的生成对抗网络（GAN）用于不同颜色通道，以去除阴影和噪声，从而促进高效的文本信息提取。然而，部署多个GAN会导致训练和推理时间较长。为减少文档图像增强和二值化模型的训练和推理时间，我们提出了MFE-GAN，这是一种基于GAN的高效框架，具有多尺度特征提取（MFE），它结合了Haar小波变换（HWT）和归一化，在将文档图像输入GAN进行训练之前进行处理。此外，我们提出了新颖的生成器、判别器和损失函数以提高模型性能，并进行了消融研究以证明其有效性。在Benchmark、Nabuco和CMATERdb数据集上的实验结果表明，所提出的MFE-GAN显著减少了总训练和推理时间，同时保持了与最先进（SOTA）方法相当的性能。本工作的实现可在https://ruiyangju.github.io/MFE-GAN获取。

## 🔬 方法详解

**问题定义**：论文旨在解决文档图像增强和二值化任务中，现有基于GAN的方法因使用多个独立网络处理不同颜色通道而导致的训练和推理时间过长问题。这限制了实际部署的效率，尤其是在处理大规模或实时文档时。

**核心思路**：论文的核心思路是通过引入多尺度特征提取（MFE）和Haar小波变换（HWT），在GAN训练前对文档图像进行预处理，从而减少模型复杂度并加速处理。这样设计是因为多尺度特征能更好地捕捉图像细节，而小波变换有助于分离噪声和阴影，使得后续GAN更高效地学习。

**技术框架**：整体框架包括预处理、生成器和判别器三阶段。预处理阶段使用Haar小波变换和归一化处理输入图像，提取多尺度特征；生成器基于这些特征生成增强和二值化图像；判别器评估生成图像的真实性。框架通过端到端训练优化性能。

**关键创新**：最重要的技术创新是集成多尺度特征提取和Haar小波变换到GAN框架中，避免了多个独立GAN的使用。与现有方法的本质区别在于，它通过预处理步骤统一处理图像，减少了模型参数和计算开销，从而显著提升效率。

**关键设计**：关键设计包括：使用Haar小波变换进行图像分解，生成多尺度特征图；设计新颖的生成器和判别器网络结构，可能基于卷积神经网络（CNN）或类似架构；损失函数结合对抗损失、内容损失（如L1或L2损失）和可能的感知损失，以平衡图像质量和二值化准确性；参数设置如学习率、批量大小等通过实验优化，具体数值未在摘要中提供，但消融研究验证了其有效性。

## 📊 实验亮点

实验在Benchmark、Nabuco和CMATERdb数据集上进行，结果显示MFE-GAN显著减少了总训练和推理时间，具体提升幅度未在摘要中量化，但强调与最先进（SOTA）方法性能相当。消融研究证明了多尺度特征提取和Haar小波变换的有效性，验证了框架在保持性能的同时优化效率的优势。

## 🎯 应用场景

该研究主要应用于文档分析和光学字符识别（OCR）领域，特别是在处理退化文档（如扫描件、历史档案或低质量图像）时。其实际价值在于通过高效增强和二值化，提升OCR系统的准确性和速度，适用于数字化图书馆、自动化办公、档案管理等场景。未来可能扩展到其他图像处理任务，如医学图像增强或视频文本识别。

## 📄 摘要（原文）

> Document image enhancement and binarization are commonly performed prior to document analysis and recognition tasks for improving the efficiency and accuracy of optical character recognition (OCR) systems. This is because directly recognizing text in degraded documents, particularly in color images, often results in unsatisfactory recognition performance. To address these issues, existing methods train independent generative adversarial networks (GANs) for different color channels to remove shadows and noise, which, in turn, facilitates efficient text information extraction. However, deploying multiple GANs results in long training and inference times. To reduce both training and inference times of document image enhancement and binarization models, we propose MFE-GAN, an efficient GAN-based framework with multi-scale feature extraction (MFE), which incorporates Haar wavelet transformation (HWT) and normalization to process document images before feeding them into GANs for training. In addition, we present novel generators, discriminators, and loss functions to improve the model's performance, and we conduct ablation studies to demonstrate their effectiveness. Experimental results on the Benchmark, Nabuco, and CMATERdb datasets demonstrate that the proposed MFE-GAN significantly reduces the total training and inference times while maintaining comparable performance with respect to state-of-the-art (SOTA) methods. The implementation of this work is available at https://ruiyangju.github.io/MFE-GAN.

