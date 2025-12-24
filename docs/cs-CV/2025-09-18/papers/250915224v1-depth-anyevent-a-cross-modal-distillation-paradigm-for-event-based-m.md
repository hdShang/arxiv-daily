---
layout: default
title: "Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation"
---

# Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15224" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15224v1</a>
  <a href="https://arxiv.org/pdf/2509.15224.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15224v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15224v1', 'Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Luca Bartolomei, Enrico Mannocci, Fabio Tosi, Matteo Poggi, Stefano Mattoccia

**分类**: cs.CV

**发布日期**: 2025-09-18

**备注**: ICCV 2025. Code: https://github.com/bartn8/depthanyevent/ Project Page: https://bartn8.github.io/depthanyevent/

---

## 💡 一句话要点

**提出基于跨模态蒸馏的事件相机单目深度估计方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事件相机` `单目深度估计` `跨模态蒸馏` `视觉基础模型` `深度学习` `代理标签` `循环神经网络`

## 📋 核心要点

1. 现有事件相机单目深度估计方法受限于缺乏大规模、带深度标注的数据集，训练困难。
2. 提出一种跨模态蒸馏范式，利用视觉基础模型（VFM）从RGB图像生成事件数据的密集代理标签。
3. 实验表明，该方法在合成和真实数据集上均表现出色，无需昂贵的深度标注即可达到SOTA性能。

## 📝 摘要（中文）

事件相机能够捕捉稀疏、高时间分辨率的视觉信息，使其特别适用于高速运动和光照条件剧烈变化等具有挑战性的环境。然而，缺乏带有密集真值深度标注的大型数据集阻碍了基于学习的事件数据单目深度估计。为了解决这个限制，我们提出了一种跨模态蒸馏范式，利用视觉基础模型（VFM）生成密集的代理标签。我们的策略需要与RGB帧空间对齐的事件流，即使是现成的设置，并利用大规模VFM的鲁棒性。此外，我们建议调整VFM，无论是像Depth Anything v2 (DAv2)这样的原始模型，还是从中派生出一种新的循环架构，以从单目事件相机推断深度。我们使用合成和真实世界数据集评估了我们的方法，证明了i) 与不需要昂贵深度标注的完全监督方法相比，我们的跨模态范式实现了具有竞争力的性能，并且 ii) 我们基于VFM的模型实现了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决事件相机单目深度估计中，由于缺乏大规模带深度标注数据集而导致的训练困难问题。现有方法要么依赖合成数据，要么需要昂贵的深度传感器进行标注，限制了其在真实场景中的应用。

**核心思路**：论文的核心思路是利用跨模态蒸馏，将视觉基础模型（VFM）在RGB图像上学习到的深度信息迁移到事件数据上。通过将RGB图像的深度预测作为事件数据的代理标签，从而避免了直接标注事件数据的需求。

**技术框架**：整体框架包含两个主要阶段：1) 代理标签生成阶段：使用预训练的VFM（如Depth Anything v2）对与事件数据同步的RGB图像进行深度预测，生成事件数据的代理深度标签。2) 事件深度估计模型训练阶段：使用生成的代理标签训练基于事件数据的深度估计模型，该模型可以是直接使用VFM进行微调，也可以是基于循环神经网络（RNN）的定制架构。

**关键创新**：该方法最重要的创新点在于提出了跨模态蒸馏范式，将RGB图像的深度信息迁移到事件数据上，从而解决了事件数据深度估计中数据标注的瓶颈问题。与现有方法相比，该方法无需昂贵的深度传感器或复杂的合成数据生成流程。

**关键设计**：关键设计包括：1) 使用Depth Anything v2等预训练VFM作为深度预测器，利用其强大的泛化能力。2) 提出基于RNN的事件深度估计模型，以适应事件数据的时序特性。3) 使用空间对齐的RGB图像和事件数据，确保代理标签的准确性。4) 损失函数采用常用的深度估计损失函数，如L1损失或Huber损失。

## 📊 实验亮点

实验结果表明，该方法在合成和真实数据集上均取得了优异的性能。与完全监督的方法相比，该方法在不需要真实深度标注的情况下，也能达到具有竞争力的性能。基于VFM的模型在多个数据集上实现了state-of-the-art的性能，证明了该跨模态蒸馏范式的有效性。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、无人机等领域，尤其是在光照条件恶劣或高速运动场景下，事件相机能够提供更可靠的深度信息。该方法降低了事件相机深度估计的数据标注成本，有望加速事件相机在实际应用中的普及。

## 📄 摘要（原文）

> Event cameras capture sparse, high-temporal-resolution visual information, making them particularly suitable for challenging environments with high-speed motion and strongly varying lighting conditions. However, the lack of large datasets with dense ground-truth depth annotations hinders learning-based monocular depth estimation from event data. To address this limitation, we propose a cross-modal distillation paradigm to generate dense proxy labels leveraging a Vision Foundation Model (VFM). Our strategy requires an event stream spatially aligned with RGB frames, a simple setup even available off-the-shelf, and exploits the robustness of large-scale VFMs. Additionally, we propose to adapt VFMs, either a vanilla one like Depth Anything v2 (DAv2), or deriving from it a novel recurrent architecture to infer depth from monocular event cameras. We evaluate our approach with synthetic and real-world datasets, demonstrating that i) our cross-modal paradigm achieves competitive performance compared to fully supervised methods without requiring expensive depth annotations, and ii) our VFM-based models achieve state-of-the-art performance.

