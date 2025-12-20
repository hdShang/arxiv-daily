---
layout: default
title: Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation
---

# Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16567" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16567v1</a>
  <a href="https://arxiv.org/pdf/2512.16567.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16567v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16567v1', 'Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yin Zhang, Yongqiang Zhang, Yaoyue Zheng, Bogdan Raducanu, Dan Liu

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**Causal-Tune：挖掘视觉基础模型中的因果因子，用于领域泛化语义分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `领域泛化` `语义分割` `视觉基础模型` `因果推断` `频率分析` `离散余弦变换` `伪影去除`

## 📋 核心要点

1. 现有领域泛化语义分割方法忽略了预训练视觉基础模型中存在的伪影，这些伪影阻碍了有价值表征的利用。
2. Causal-Tune通过显式地识别和分离视觉基础模型特征中的因果和非因果因素，从而实现更鲁棒的领域泛化。
3. 实验表明，Causal-Tune在各种跨域任务中表现出色，尤其是在恶劣天气条件下，显著提升了语义分割的性能。

## 📝 摘要（中文）

本文提出了一种针对领域泛化语义分割（DGSS）的因果调优（Causal-Tune）方法，旨在解决视觉基础模型（VFM）中存在的伪影问题。作者观察到，这些伪影与VFM频谱中的低频和高频非因果因素相关。Causal-Tune显式地检查VFM特征中的因果和非因果因素，并通过离散余弦变换（DCT）提取每一层的特征频谱，然后应用高斯带通滤波器将频谱分离为因果和非因果分量。为了进一步提炼因果分量，引入了一组在频域中运行的因果感知可学习tokens，并丢弃非因果分量。最后，将精炼后的特征通过逆DCT转换回空间域，并传递到下一层。在各种跨域任务上的大量实验表明了Causal-Tune的有效性，尤其是在恶劣天气条件下，与基线相比，在雪地条件下提高了+4.8%的mIoU。

## 🔬 方法详解

**问题定义**：领域泛化语义分割（DGSS）旨在使模型在未见过的目标领域上也能保持良好的分割性能。现有的方法，如微调轻量级适配器或优化中间层特征，忽略了预训练视觉基础模型（VFM）中存在的伪影。这些伪影通常与非因果因素相关，阻碍了VFM中宝贵表征的利用，最终降低了DGSS的性能。

**核心思路**：本文的核心思路是基于因果机制，将VFM特征分解为因果因素和非因果因素，并抑制非因果因素的影响，从而提高模型的泛化能力。作者观察到，这些非因果因素通常存在于VFM频谱的低频和高频分量中。通过提取和过滤这些频率分量，可以有效地去除伪影，并保留对语义分割任务有用的因果信息。

**技术框架**：Causal-Tune的整体框架包括以下几个主要步骤：1) 使用离散余弦变换（DCT）提取VFM每一层特征的频率频谱。2) 应用高斯带通滤波器将频谱分离为因果和非因果分量。3) 引入一组因果感知可学习tokens，在频域中操作，以进一步提炼因果分量。4) 丢弃非因果分量。5) 使用逆DCT将精炼后的特征转换回空间域，并传递到下一层。

**关键创新**：Causal-Tune的关键创新在于显式地建模和分离VFM特征中的因果和非因果因素。与以往的方法不同，Causal-Tune不是简单地微调整个VFM，而是有选择性地保留和增强因果信息，同时抑制非因果噪声。这种方法能够更有效地利用VFM的预训练知识，并提高模型在未见领域上的泛化能力。

**关键设计**：高斯带通滤波器的参数（例如中心频率和带宽）需要根据具体的VFM和数据集进行调整，以实现最佳的因果/非因果分离效果。因果感知可学习tokens的设计也至关重要，它们需要能够有效地捕捉频域中的因果信息，并抑制噪声。损失函数的设计也需要考虑如何鼓励模型学习更鲁棒的因果表征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16567v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Causal-Tune在多个跨域语义分割任务上取得了显著的性能提升。特别是在恶劣天气条件下，例如雪地场景，Causal-Tune相比基线方法提高了+4.8%的mIoU。这些实验结果表明，Causal-Tune能够有效地提取因果因素并抑制非因果因素，从而提高模型的泛化能力。

## 🎯 应用场景

Causal-Tune在自动驾驶、机器人视觉、遥感图像分析等领域具有广泛的应用前景。通过提高模型在不同环境和条件下的鲁棒性，可以显著提升这些应用系统的可靠性和安全性。例如，在自动驾驶中，Causal-Tune可以帮助车辆更好地应对恶劣天气条件，从而减少交通事故的发生。

## 📄 摘要（原文）

> Fine-tuning Vision Foundation Models (VFMs) with a small number of parameters has shown remarkable performance in Domain Generalized Semantic Segmentation (DGSS). Most existing works either train lightweight adapters or refine intermediate features to achieve better generalization on unseen domains. However, they both overlook the fact that long-term pre-trained VFMs often exhibit artifacts, which hinder the utilization of valuable representations and ultimately degrade DGSS performance. Inspired by causal mechanisms, we observe that these artifacts are associated with non-causal factors, which usually reside in the low- and high-frequency components of the VFM spectrum. In this paper, we explicitly examine the causal and non-causal factors of features within VFMs for DGSS, and propose a simple yet effective method to identify and disentangle them, enabling more robust domain generalization. Specifically, we propose Causal-Tune, a novel fine-tuning strategy designed to extract causal factors and suppress non-causal ones from the features of VFMs. First, we extract the frequency spectrum of features from each layer using the Discrete Cosine Transform (DCT). A Gaussian band-pass filter is then applied to separate the spectrum into causal and non-causal components. To further refine the causal components, we introduce a set of causal-aware learnable tokens that operate in the frequency domain, while the non-causal components are discarded. Finally, refined features are transformed back into the spatial domain via inverse DCT and passed to the next layer. Extensive experiments conducted on various cross-domain tasks demonstrate the effectiveness of Causal-Tune. In particular, our method achieves superior performance under adverse weather conditions, improving +4.8% mIoU over the baseline in snow conditions.

