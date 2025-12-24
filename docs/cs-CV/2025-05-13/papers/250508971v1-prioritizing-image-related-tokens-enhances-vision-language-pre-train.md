---
layout: default
title: Prioritizing Image-Related Tokens Enhances Vision-Language Pre-Training
---

# Prioritizing Image-Related Tokens Enhances Vision-Language Pre-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08971" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08971v1</a>
  <a href="https://arxiv.org/pdf/2505.08971.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08971v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08971v1', 'Prioritizing Image-Related Tokens Enhances Vision-Language Pre-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yangyi Chen, Hao Peng, Tong Zhang, Heng Ji

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-05-13

**备注**: The code will be available at https://github.com/Yangyi-Chen/PRIOR

---

## 💡 一句话要点

**提出PRIOR以解决视觉语言模型中的噪声问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `下一个标记预测` `重要性采样` `多模态学习` `模型优化` `图像描述生成` `幻觉问题`

## 📋 核心要点

1. 现有的视觉语言模型在预训练过程中，容易受到与视觉内容无关的噪声影响，导致模型性能下降。
2. 论文提出的PRIOR方法通过对图像相关标记进行差异加权，优化了下一个标记预测的损失函数，提升了模型的学习效果。
3. 实验结果显示，PRIOR在多个视觉语言基准上相较于NTP分别提升了19%和8%的性能，且具有更好的扩展性。

## 📝 摘要（中文）

在标准的大型视觉语言模型（LVLMs）预训练中，模型通常通过下一个标记预测（NTP）最大化图像条件下的字幕联合概率。然而，由于只有一小部分字幕标记与视觉内容直接相关，这种简单的NTP无意中使模型适应噪声，增加了幻觉的风险。我们提出了PRIOR，这是一种简单的视觉语言预训练方法，通过在NTP损失中对图像相关标记进行差异加权来解决这一问题。PRIOR引入了一个参考模型——一个仅基于文本的大型语言模型（LLM），用于根据其在没有图像输入的情况下的概率来加权每个标记。通过这种方式，直接与视觉输入相关的标记在没有图像的情况下更难预测，因此从文本参考LLM获得的概率较低。我们在两个不同的设置中实现了PRIOR，并在多个视觉语言基准上观察到相较于NTP分别有19%和8%的平均相对提升。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有视觉语言模型在预训练中容易受到与视觉内容无关的噪声影响，导致模型在生成字幕时出现幻觉现象。现有的下一个标记预测（NTP）方法未能有效区分与图像内容相关的标记和无关标记。

**核心思路**：PRIOR方法的核心思路是通过引入一个文本参考模型，对每个标记进行差异加权，从而在损失函数中优先考虑与图像相关的标记。这种设计使得模型在训练过程中更加关注重要的视觉信息，减少了噪声的影响。

**技术框架**：PRIOR的整体架构包括两个主要模块：一个是图像输入的视觉编码器，另一个是文本参考模型。训练过程中，模型根据文本参考模型的输出对每个标记的损失进行调整，以实现更有效的学习。

**关键创新**：PRIOR的最重要技术创新在于通过重要性采样框架引入了标记的差异加权机制。这一机制使得模型能够更好地识别与视觉内容相关的标记，从而显著提升了生成字幕的准确性。

**关键设计**：在损失函数中，PRIOR引入了一个标记特定的重加权项，基于文本参考模型的概率对每个标记进行加权。此外，模型在不同设置下的实现也展示了其灵活性，包括有无视觉编码器的情况。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果表明，PRIOR在多个视觉语言基准上相较于传统的NTP方法分别实现了19%和8%的平均相对提升。此外，PRIOR在扩展性方面表现优越，显示出在计算和数据增加时更大的性能提升潜力。

## 🎯 应用场景

该研究的潜在应用领域包括图像描述生成、视觉问答和多模态内容检索等。通过提高视觉语言模型的准确性，PRIOR能够在实际应用中提供更为可靠的结果，推动智能助手、自动内容生成等技术的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In standard large vision-language models (LVLMs) pre-training, the model typically maximizes the joint probability of the caption conditioned on the image via next-token prediction (NTP); however, since only a small subset of caption tokens directly relates to the visual content, this naive NTP unintentionally fits the model to noise and increases the risk of hallucination. We present PRIOR, a simple vision-language pre-training approach that addresses this issue by prioritizing image-related tokens through differential weighting in the NTP loss, drawing from the importance sampling framework. PRIOR introduces a reference model-a text-only large language model (LLM) trained on the captions without image inputs, to weight each token based on its probability for LVLMs training. Intuitively, tokens that are directly related to the visual inputs are harder to predict without the image and thus receive lower probabilities from the text-only reference LLM. During training, we implement a token-specific re-weighting term based on the importance scores to adjust each token's loss. We implement PRIOR in two distinct settings: LVLMs with visual encoders and LVLMs without visual encoders. We observe 19% and 8% average relative improvement, respectively, on several vision-language benchmarks compared to NTP. In addition, PRIOR exhibits superior scaling properties, as demonstrated by significantly higher scaling coefficients, indicating greater potential for performance gains compared to NTP given increasing compute and data.

