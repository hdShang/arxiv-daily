---
layout: default
title: A Dual-Branch CNN for Robust Detection of AI-Generated Facial Forgeries
---

# A Dual-Branch CNN for Robust Detection of AI-Generated Facial Forgeries

**arXiv**: [2510.24640v1](https://arxiv.org/abs/2510.24640) | [PDF](https://arxiv.org/pdf/2510.24640.pdf)

**作者**: Xin Zhang, Yuqi Song, Fei Zuo

---

## 💡 一句话要点

**提出双分支CNN以检测AI生成面部伪造，提升AI安全与媒体完整性**

**关键词**: `面部伪造检测` `双分支CNN` `频域分析` `通道注意力` `统一损失函数` `AI安全`

## 📋 核心要点

1. 核心问题：生成AI技术导致面部伪造图像泛滥，威胁AI安全与数字媒体可信度。
2. 方法要点：结合空间与频域分支，使用通道注意力融合特征，设计统一损失函数增强鲁棒性。
3. 实验或效果：在DiFF基准测试中表现优异，超越人类平均准确率，验证模型有效性。

## 📄 摘要（原文）

> The rapid advancement of generative AI has enabled the creation of highly
> realistic forged facial images, posing significant threats to AI security,
> digital media integrity, and public trust. Face forgery techniques, ranging
> from face swapping and attribute editing to powerful diffusion-based image
> synthesis, are increasingly being used for malicious purposes such as
> misinformation, identity fraud, and defamation. This growing challenge
> underscores the urgent need for robust and generalizable face forgery detection
> methods as a critical component of AI security infrastructure. In this work, we
> propose a novel dual-branch convolutional neural network for face forgery
> detection that leverages complementary cues from both spatial and frequency
> domains. The RGB branch captures semantic information, while the frequency
> branch focuses on high-frequency artifacts that are difficult for generative
> models to suppress. A channel attention module is introduced to adaptively fuse
> these heterogeneous features, highlighting the most informative channels for
> forgery discrimination. To guide the network's learning process, we design a
> unified loss function, FSC Loss, that combines focal loss, supervised
> contrastive loss, and a frequency center margin loss to enhance class
> separability and robustness. We evaluate our model on the DiFF benchmark, which
> includes forged images generated from four representative methods:
> text-to-image, image-to-image, face swap, and face edit. Our method achieves
> strong performance across all categories and outperforms average human
> accuracy. These results demonstrate the model's effectiveness and its potential
> contribution to safeguarding AI ecosystems against visual forgery attacks.

