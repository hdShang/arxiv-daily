---
layout: default
title: "MMFformer: Multimodal Fusion Transformer Network for Depression Detection"
---

# MMFformer: Multimodal Fusion Transformer Network for Depression Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06701" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06701v1</a>
  <a href="https://arxiv.org/pdf/2508.06701.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06701v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06701v1', 'MMFformer: Multimodal Fusion Transformer Network for Depression Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Rezwanul Haque, Md. Milon Islam, S M Taslim Uddin Raju, Hamdi Altaheri, Lobna Nassar, Fakhri Karray

**分类**: cs.CV, cs.AI, cs.CL, cs.LG, cs.SD, eess.AS

**发布日期**: 2025-08-08

**备注**: Accepted for the 2025 IEEE International Conference on Systems, Man, and Cybernetics (SMC), Vienna, Austria

**🔗 代码/项目**: [GITHUB](https://github.com/rezwanh001/Large-Scale-Multimodal-Depression-Detection)

---

## 💡 一句话要点

**提出MMFformer以解决多模态抑郁检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态融合` `抑郁症检测` `变换器网络` `社交媒体分析` `时空特征提取`

## 📋 核心要点

1. 现有抑郁症检测方法主要依赖主观评估，难以准确捕捉用户情绪变化，尤其是在多模态社交媒体数据中。
2. MMFformer通过多模态融合变换器网络，结合视频和音频特征，提取抑郁症的时空模式，提升检测准确性。
3. 在D-Vlog和LMVD数据集上，MMFformer的F1分数分别提高了13.92%和7.74%，显示出显著的性能提升。

## 📝 摘要（中文）

抑郁症是一种严重的心理健康疾病，显著影响个体的幸福感和生活质量，因此早期检测至关重要。抑郁症的检测通常依赖于临床访谈中的主观评估，难度较大。基于社交网络内容的早期诊断已成为一个重要的研究领域。用户生成信息的广泛性和多样性给相关时序信息的准确提取和多模态数据的有效融合带来了挑战。本文提出了MMFformer，一个多模态抑郁检测网络，旨在从多模态社交媒体信息中提取抑郁的时空高层模式。该网络通过残差连接的变换器捕捉视频的空间特征，并利用变换器编码器设计音频中的重要时序动态。此外，融合架构通过晚期和中期融合策略融合提取的特征，以发现它们之间最相关的跨模态关联。实验结果表明，该网络在两个大规模抑郁检测数据集上超越了现有的最先进方法，D-Vlog数据集的F1分数提高了13.92%，LMVD数据集提高了7.74%。

## 🔬 方法详解

**问题定义**：本文旨在解决抑郁症检测中的多模态数据融合问题。现有方法往往无法有效提取社交媒体中用户情绪的时序特征，导致检测准确性不足。

**核心思路**：MMFformer通过设计一个多模态融合变换器网络，利用视频和音频数据的空间和时序特征，来提高抑郁症的检测能力。该设计旨在捕捉不同模态之间的相关性，从而更全面地理解用户情绪。

**技术框架**：该网络包括视频特征提取模块、音频特征提取模块和融合模块。视频模块使用变换器网络捕捉空间特征，音频模块则通过变换器编码器提取时序动态，最后通过晚期和中期融合策略整合这些特征。

**关键创新**：MMFformer的主要创新在于其多模态融合策略，能够有效捕捉视频和音频之间的时空关联，显著提升了抑郁症检测的准确性。这一方法与传统的单一模态检测方法相比，具有更高的灵活性和准确性。

**关键设计**：在网络设计中，采用了残差连接以增强特征提取的能力，损失函数则针对多模态特征的融合进行了优化，确保了不同模态信息的有效整合。

## 📊 实验亮点

MMFformer在D-Vlog和LMVD数据集上的实验结果显示，F1分数分别提高了13.92%和7.74%，显著超越了现有的最先进方法。这一提升表明该模型在多模态抑郁检测中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康监测、社交媒体情绪分析和智能医疗系统。通过早期检测抑郁症，能够为患者提供及时的干预和支持，提升整体社会心理健康水平。未来，该技术还可以扩展到其他心理健康问题的检测与分析中。

## 📄 摘要（原文）

> Depression is a serious mental health illness that significantly affects an individual's well-being and quality of life, making early detection crucial for adequate care and treatment. Detecting depression is often difficult, as it is based primarily on subjective evaluations during clinical interviews. Hence, the early diagnosis of depression, thanks to the content of social networks, has become a prominent research area. The extensive and diverse nature of user-generated information poses a significant challenge, limiting the accurate extraction of relevant temporal information and the effective fusion of data across multiple modalities. This paper introduces MMFformer, a multimodal depression detection network designed to retrieve depressive spatio-temporal high-level patterns from multimodal social media information. The transformer network with residual connections captures spatial features from videos, and a transformer encoder is exploited to design important temporal dynamics in audio. Moreover, the fusion architecture fused the extracted features through late and intermediate fusion strategies to find out the most relevant intermodal correlations among them. Finally, the proposed network is assessed on two large-scale depression detection datasets, and the results clearly reveal that it surpasses existing state-of-the-art approaches, improving the F1-Score by 13.92% for D-Vlog dataset and 7.74% for LMVD dataset. The code is made available publicly at https://github.com/rezwanh001/Large-Scale-Multimodal-Depression-Detection.

