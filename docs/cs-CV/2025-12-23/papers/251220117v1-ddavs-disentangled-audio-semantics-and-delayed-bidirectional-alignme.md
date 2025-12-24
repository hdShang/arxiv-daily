---
layout: default
title: DDAVS: Disentangled Audio Semantics and Delayed Bidirectional Alignment for Audio-Visual Segmentation
---

# DDAVS: Disentangled Audio Semantics and Delayed Bidirectional Alignment for Audio-Visual Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20117" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20117v1</a>
  <a href="https://arxiv.org/pdf/2512.20117.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20117v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20117v1', 'DDAVS: Disentangled Audio Semantics and Delayed Bidirectional Alignment for Audio-Visual Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingqi Tian, Yiheng Du, Haoji Zhang, Yuji Wang, Isaac Ning Lee, Xulong Bai, Tianrui Zhu, Jingxuan Niu, Yansong Tang

**分类**: cs.CV, cs.SD, eess.AS

**发布日期**: 2025-12-23

**备注**: https://trilarflagz.github.io/DDAVS-page/

**🔗 代码/项目**: [PROJECT_PAGE](https://trilarflagz.github.io/DDAVS-page/)

---

## 💡 一句话要点

**DDAVS：解耦音频语义与延迟双向对齐，用于音视频分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频分割` `多模态融合` `语义解耦` `交叉注意力` `对比学习`

## 📋 核心要点

1. 现有音视频分割方法易受多源混淆和模态未对齐影响，导致分割结果偏向显著物体。
2. DDAVS通过解耦音频语义和延迟双向对齐，提升模型对弱小和共现声源的分割能力。
3. 实验表明，DDAVS在单源、多源和多实例场景下均优于现有方法，验证了其有效性。

## 📝 摘要（中文）

音视频分割(AVS)旨在通过联合利用听觉和视觉信息，在像素级别定位发声物体。然而，现有方法常常受到多源纠缠和音视频未对齐的影响，导致模型偏向于响亮或较大的物体，而忽略较弱、较小或同时出现的声源。为了解决这些挑战，我们提出了DDAVS，一个解耦音频语义和延迟双向对齐框架。为了缓解多源纠缠，DDAVS采用可学习的查询来提取音频语义，并将它们锚定在从音频原型记忆库导出的结构化语义空间中。通过对比学习进一步优化，以增强可区分性和鲁棒性。为了减轻音视频未对齐，DDAVS引入了具有延迟模态交互的双重交叉注意力，提高了多模态对齐的鲁棒性。在AVS-Objects和VPO基准上的大量实验表明，DDAVS始终优于现有方法，在单源、多源和多实例场景中表现出强大的性能。这些结果验证了我们的框架在具有挑战性的真实世界音视频分割条件下的有效性和泛化能力。

## 🔬 方法详解

**问题定义**：音视频分割(AVS)旨在像素级别定位发声物体。现有方法的痛点在于：1)多源纠缠，即模型难以区分和分割多个同时发声的物体，容易偏向于响亮或较大的物体；2)音视频未对齐，由于时序和空间上的差异，音频和视频特征难以有效融合，影响分割精度。

**核心思路**：DDAVS的核心思路是解耦音频语义，并采用延迟双向对齐来解决上述问题。具体来说，通过可学习的查询和音频原型记忆库，将音频语义映射到结构化的语义空间，从而减少多源之间的干扰。同时，通过延迟模态交互的双重交叉注意力机制，增强音视频特征的对齐和融合。

**技术框架**：DDAVS框架主要包含以下几个模块：1)音频特征提取模块，用于提取音频的语义特征；2)可学习查询模块，用于从音频特征中提取关键语义信息；3)音频原型记忆库，用于构建结构化的音频语义空间；4)对比学习模块，用于增强音频语义的可区分性；5)双重交叉注意力模块，用于实现音视频特征的对齐和融合；6)分割头，用于生成最终的分割结果。

**关键创新**：DDAVS的关键创新在于：1)解耦音频语义，通过可学习查询和音频原型记忆库，将音频语义映射到结构化的语义空间，减少多源干扰；2)延迟双向对齐，通过双重交叉注意力机制，并延迟模态交互，增强音视频特征的对齐和融合，提高分割精度。

**关键设计**：音频原型记忆库的设计是关键。它通过聚类音频特征来构建原型，并使用对比学习来优化原型表示，从而增强音频语义的可区分性。双重交叉注意力模块采用延迟模态交互，即先在各自模态内进行自注意力计算，再进行跨模态的交叉注意力计算，避免了早期融合可能导致的信息损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20117v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20117v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20117v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DDAVS在AVS-Objects和VPO基准测试中均取得了显著的性能提升。在AVS-Objects数据集上，DDAVS的mIoU指标优于现有最佳方法，尤其在多源和多实例场景下提升显著。在VPO数据集上，DDAVS也取得了具有竞争力的结果，验证了其泛化能力。

## 🎯 应用场景

DDAVS在智能监控、自动驾驶、机器人等领域具有广泛的应用前景。例如，在智能监控中，可以利用DDAVS定位异常声音事件发生的位置；在自动驾驶中，可以帮助车辆感知周围环境中的声源，提高安全性；在机器人领域，可以使机器人更好地理解和交互周围环境。

## 📄 摘要（原文）

> Audio-Visual Segmentation (AVS) aims to localize sound-producing objects at the pixel level by jointly leveraging auditory and visual information. However, existing methods often suffer from multi-source entanglement and audio-visual misalignment, which lead to biases toward louder or larger objects while overlooking weaker, smaller, or co-occurring sources. To address these challenges, we propose DDAVS, a Disentangled Audio Semantics and Delayed Bidirectional Alignment framework. To mitigate multi-source entanglement, DDAVS employs learnable queries to extract audio semantics and anchor them within a structured semantic space derived from an audio prototype memory bank. This is further optimized through contrastive learning to enhance discriminability and robustness. To alleviate audio-visual misalignment, DDAVS introduces dual cross-attention with delayed modality interaction, improving the robustness of multimodal alignment. Extensive experiments on the AVS-Objects and VPO benchmarks demonstrate that DDAVS consistently outperforms existing approaches, exhibiting strong performance across single-source, multi-source, and multi-instance scenarios. These results validate the effectiveness and generalization ability of our framework under challenging real-world audio-visual segmentation conditions. Project page: https://trilarflagz.github.io/DDAVS-page/

