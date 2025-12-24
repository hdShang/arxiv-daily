---
layout: default
title: "SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models"
---

# SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15536" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15536v2</a>
  <a href="https://arxiv.org/pdf/2509.15536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15536v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15536v2', 'SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sen Wang, Jingyi Tian, Le Wang, Zhimin Liao, Jiayi Li, Huaiyi Dong, Kun Xia, Sanping Zhou, Wei Tang, Hua Gang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-19 (更新: 2025-10-21)

**备注**: 22 pages,15 figures

---

## 💡 一句话要点

**SAMPO：基于运动提示的分尺度自回归生成世界模型，提升视频预测质量与效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `世界模型` `视频预测` `自回归模型` `运动建模` `机器人控制`

## 📋 核心要点

1. 现有自回归世界模型在空间结构保持、解码效率和运动建模方面存在不足，导致视觉连贯性预测困难。
2. SAMPO通过结合视觉自回归和因果建模，利用双向空间注意力和运动提示，提升时间一致性和rollout效率。
3. 实验表明，SAMPO在视频预测和模型控制方面表现出色，推理速度提升4.4倍，并具备良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种名为SAMPO（基于运动提示的分尺度自回归）的混合框架，用于解决现有自回归世界模型在视觉连贯性预测、解码效率和运动建模方面的不足。SAMPO结合了视觉自回归建模进行帧内生成和因果建模进行下一帧生成。它集成了时间因果解码与双向空间注意力，从而保持空间局部性并支持每个尺度内的并行解码，显著提高了时间一致性和rollout效率。此外，设计了一种非对称多尺度tokenizer，保留了观测帧中的空间细节，并为未来帧提取紧凑的动态表示，优化了内存使用和模型性能。引入了轨迹感知的运动提示模块，注入了关于对象和机器人轨迹的时空线索，将注意力集中在动态区域，并改善了时间一致性和物理真实感。实验表明，SAMPO在动作条件视频预测和基于模型的控制方面取得了有竞争力的性能，并在生成质量方面有所提高，同时推理速度提高了4.4倍。SAMPO还展示了其零样本泛化能力和扩展性，能够泛化到未见过的任务并受益于更大的模型尺寸。

## 🔬 方法详解

**问题定义**：现有自回归世界模型在生成视频时，由于空间结构的破坏、解码效率低下以及运动建模不足，难以产生视觉上连贯的预测结果。这限制了它们在需要长期规划和控制任务中的应用。

**核心思路**：SAMPO的核心思路是将帧内生成和帧间生成解耦，分别使用视觉自回归建模和因果建模。通过分尺度处理，在每个尺度上利用双向空间注意力保持空间局部性，并实现并行解码，从而提高效率和连贯性。运动提示模块则显式地建模了物体和机器人的运动轨迹，引导模型关注动态区域。

**技术框架**：SAMPO的整体框架包含以下几个主要模块：1) 非对称多尺度Tokenizer：用于提取输入视频帧的多尺度特征表示，对观测帧和未来帧采用不同的处理方式，以保留空间细节并提取紧凑的动态表示。2) 分尺度自回归生成器：利用时间因果解码和双向空间注意力，在每个尺度上自回归地生成下一帧的特征表示。3) 运动提示模块：注入轨迹感知的运动信息，引导生成器关注动态区域。

**关键创新**：SAMPO的关键创新在于以下几个方面：1) 混合建模：结合了视觉自回归和因果建模，分别处理帧内和帧间生成。2) 分尺度处理：在多个尺度上进行自回归生成，提高了效率和连贯性。3) 运动提示：显式地建模了运动信息，提高了生成结果的物理真实感。与现有方法相比，SAMPO更有效地利用了空间和时间信息，从而提高了生成质量和效率。

**关键设计**：非对称多尺度Tokenizer的设计旨在平衡空间细节的保留和动态信息的提取。运动提示模块通过编码物体和机器人的轨迹信息，并将其注入到生成器中，引导模型关注动态区域。损失函数可能包含重建损失和对抗损失等，以提高生成结果的质量和真实感。具体的网络结构和参数设置未知。

## 📊 实验亮点

实验结果表明，SAMPO在动作条件视频预测和基于模型的控制任务中取得了有竞争力的性能。与现有方法相比，SAMPO在生成质量方面有所提高，并且推理速度提高了4.4倍。此外，SAMPO还展示了良好的零样本泛化能力和扩展性，能够泛化到未见过的任务并受益于更大的模型尺寸。具体的性能指标和对比基线未知。

## 🎯 应用场景

SAMPO具有广泛的应用前景，包括机器人控制、自动驾驶、游戏AI和视频生成等领域。它可以用于训练智能体在虚拟环境中进行长期规划和决策，提高智能体的自主性和适应性。此外，SAMPO还可以用于生成高质量的视频内容，例如电影特效和游戏动画。

## 📄 摘要（原文）

> World models allow agents to simulate the consequences of actions in imagined environments for planning, control, and long-horizon decision-making. However, existing autoregressive world models struggle with visually coherent predictions due to disrupted spatial structure, inefficient decoding, and inadequate motion modeling. In response, we propose \textbf{S}cale-wise \textbf{A}utoregression with \textbf{M}otion \textbf{P}r\textbf{O}mpt (\textbf{SAMPO}), a hybrid framework that combines visual autoregressive modeling for intra-frame generation with causal modeling for next-frame generation. Specifically, SAMPO integrates temporal causal decoding with bidirectional spatial attention, which preserves spatial locality and supports parallel decoding within each scale. This design significantly enhances both temporal consistency and rollout efficiency. To further improve dynamic scene understanding, we devise an asymmetric multi-scale tokenizer that preserves spatial details in observed frames and extracts compact dynamic representations for future frames, optimizing both memory usage and model performance. Additionally, we introduce a trajectory-aware motion prompt module that injects spatiotemporal cues about object and robot trajectories, focusing attention on dynamic regions and improving temporal consistency and physical realism. Extensive experiments show that SAMPO achieves competitive performance in action-conditioned video prediction and model-based control, improving generation quality with 4.4$\times$ faster inference. We also evaluate SAMPO's zero-shot generalization and scaling behavior, demonstrating its ability to generalize to unseen tasks and benefit from larger model sizes.

