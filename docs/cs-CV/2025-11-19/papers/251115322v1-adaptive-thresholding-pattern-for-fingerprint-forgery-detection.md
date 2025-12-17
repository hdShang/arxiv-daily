---
layout: default
title: Adaptive thresholding pattern for fingerprint forgery detection
---

# Adaptive thresholding pattern for fingerprint forgery detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15322" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15322v1</a>
  <a href="https://arxiv.org/pdf/2511.15322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15322v1" onclick="toggleFavorite(this, '2511.15322v1', 'Adaptive thresholding pattern for fingerprint forgery detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zahra Farzadpour, Masoumeh Azghani

**分类**: cs.CV

**发布日期**: 2025-11-19

**备注**: 25 pages, 10 figures, Journal paper

**期刊**: Farzadpour, Z., & Azghani, M. (2024). Adaptive thresholding pattern for fingerprint forgery detection. Multimedia Tools and Applications, 83(34), 81665-81683

**DOI**: [10.1007/s11042-024-18649-3](https://doi.org/10.1007/s11042-024-18649-3)

---

## 💡 一句话要点

**提出基于自适应阈值模式的指纹伪造检测算法，提升抗干扰能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `指纹伪造检测` `活性检测` `自适应阈值` `小波变换` `各向异性扩散`

## 📋 核心要点

1. 现有指纹活性检测易受伪造攻击，且对噪声、像素缺失等干扰敏感，降低了生物识别系统的安全性。
2. 提出一种基于自适应阈值模式的指纹伪造检测算法，旨在提高系统对各种失真的鲁棒性。
3. 实验结果表明，该方法在像素和块缺失等场景下，检测准确率显著优于现有方法，提升效果明显。

## 📝 摘要（中文）

指纹活性检测系统容易受到欺骗攻击，这对基于指纹的生物识别系统构成了严重威胁。因此，开发区分真假指纹的技术至关重要。本文提出了一种基于自适应阈值模式的指纹伪造检测算法。该算法首先对输入图像进行各向异性扩散，然后进行三层小波变换。不同层的小波系数经过自适应阈值处理并连接，生成特征向量，最后使用SVM分类器进行分类。本文的另一个贡献是研究了各种失真（如像素缺失、块缺失和噪声污染）的影响。该方法对环境现象或恶意用户操作引起的各种失真具有更强的鲁棒性。定量比较表明，在像素缺失90%和块缺失尺寸为70x70的情况下，该方法的准确率分别比同类方法高出约8%和5%。

## 🔬 方法详解

**问题定义**：指纹识别系统面临伪造指纹的威胁，现有的指纹活性检测方法容易受到各种失真（如噪声、像素缺失、块缺失）的影响，导致检测准确率下降。攻击者可以通过在伪造指纹中添加这些失真来欺骗检测器。因此，需要一种能够抵抗这些失真的指纹伪造检测算法。

**核心思路**：该论文的核心思路是利用自适应阈值模式提取指纹图像的特征，并结合小波变换和各向异性扩散来增强图像的鲁棒性。通过自适应地调整阈值，可以更好地适应不同类型的失真，从而提高检测的准确性。

**技术框架**：该算法的整体流程如下：1) 对输入指纹图像进行各向异性扩散，以平滑噪声并增强图像的结构信息。2) 对扩散后的图像进行三层小波变换，提取不同尺度的特征。3) 对不同层的小波系数进行自适应阈值处理，去除噪声和不重要的特征。4) 将阈值处理后的系数连接成特征向量。5) 使用SVM分类器对特征向量进行分类，判断指纹的真伪。

**关键创新**：该论文的关键创新在于提出了自适应阈值模式，该模式能够根据图像的局部特征动态地调整阈值，从而更好地适应不同类型的失真。此外，该论文还研究了各种失真对指纹伪造检测的影响，并提出了相应的应对策略。

**关键设计**：自适应阈值的具体计算方法未知，论文中没有详细说明。各向异性扩散的具体参数设置也未知。SVM分类器的核函数和参数选择也未知。这些细节会影响算法的性能。

## 📊 实验亮点

实验结果表明，该方法在像素缺失90%的情况下，检测准确率比同类方法高出约8%；在块缺失尺寸为70x70的情况下，准确率高出约5%。这些结果表明，该方法对各种失真具有较强的鲁棒性，能够有效提高指纹伪造检测的准确率。

## 🎯 应用场景

该研究成果可应用于各种需要指纹识别的场景，例如门禁系统、移动支付、身份验证等。通过提高指纹识别系统对伪造指纹的抵抗能力，可以有效防止欺诈行为，提高系统的安全性。未来，该技术可以与其他生物识别技术相结合，构建更安全可靠的身份验证系统。

## 📄 摘要（原文）

> Fingerprint liveness detection systems have been affected by spoofing, which is a severe threat for fingerprint-based biometric systems. Therefore, it is crucial to develop some techniques to distinguish the fake fingerprints from the real ones. The software based techniques can detect the fingerprint forgery automatically. Also, the scheme shall be resistant against various distortions such as noise contamination, pixel missing and block missing, so that the forgers cannot deceive the detector by adding some distortions to the faked fingerprint. In this paper, we propose a fingerprint forgery detection algorithm based on a suggested adaptive thresholding pattern. The anisotropic diffusion of the input image is passed through three levels of the wavelet transform. The coefficients of different layers are adaptively thresholded and concatenated to produce the feature vector which is classified using the SVM classifier. Another contribution of the paper is to investigate the effect of various distortions such as pixel missing, block missing, and noise contamination. Our suggested approach includes a novel method that exhibits improved resistance against a range of distortions caused by environmental phenomena or manipulations by malicious users. In quantitative comparisons, our proposed method outperforms its counterparts by approximately 8% and 5% in accuracy for missing pixel scenarios of 90% and block missing scenarios of size 70x70 , respectively. This highlights the novelty approach in addressing such challenges.

