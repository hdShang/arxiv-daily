---
layout: default
title: SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model
---

# SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22039" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22039v1</a>
  <a href="https://arxiv.org/pdf/2511.22039.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22039v1" onclick="toggleFavorite(this, '2511.22039v1', 'SparseWorld-TC: Trajectory-Conditioned Sparse Occupancy World Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayuan Du, Yiming Zhao, Zhenglong Guo, Yong Pan, Wenbo Hou, Zhihui Hao, Kun Zhan, Qijun Chen

**分类**: cs.CV

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**提出轨迹条件下的稀疏Occupancy World Model，用于未来3D场景Occupancy预测。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `Occupancy预测` `稀疏表征` `Transformer` `自动驾驶` `场景理解`

## 📋 核心要点

1. 现有方法依赖VAE生成离散Occupancy tokens，限制了表征能力，且BEV投影引入了结构限制。
2. 该方法采用稀疏Occupancy表征，绕过BEV投影，直接从图像特征端到端预测未来Occupancy。
3. 实验表明，该方法在nuScenes数据集上实现了SOTA性能，且对未来轨迹条件具有鲁棒性。

## 📝 摘要（中文）

本文提出了一种新颖的架构，用于轨迹条件下的未来3D场景Occupancy预测。与依赖变分自编码器(VAEs)生成离散Occupancy tokens的方法不同（此类方法固有地限制了表征能力），我们的方法直接从原始图像特征以端到端的方式预测多帧未来Occupancy。受到基于注意力机制的Transformer架构在GPT和VGGT等基础视觉和语言模型中取得的成功的启发，我们采用了一种稀疏Occupancy表征，它绕过了中间的鸟瞰图(BEV)投影及其显式的几何先验。这种设计使得Transformer能够更有效地捕获时空依赖关系。通过避免离散tokenization的有限容量约束和BEV表征的结构限制，我们的方法在nuScenes基准测试中实现了1-3秒Occupancy预测的最先进性能，显著优于现有方法。此外，它展示了强大的场景动态理解能力，在任意未来轨迹条件下始终提供高精度。

## 🔬 方法详解

**问题定义**：现有方法在预测未来3D场景Occupancy时，通常依赖于变分自编码器（VAEs）来生成离散的Occupancy tokens，这种方法的缺点在于离散tokenization限制了表征能力。此外，一些方法使用鸟瞰图（BEV）投影，虽然引入了几何先验，但也限制了模型对复杂时空关系的建模能力。因此，如何更有效地表征和预测未来场景的Occupancy成为一个挑战。

**核心思路**：本文的核心思路是采用一种稀疏Occupancy表征，并利用Transformer架构直接从原始图像特征预测未来Occupancy，从而避免了离散tokenization的容量限制和BEV投影的结构限制。通过这种方式，模型可以更有效地学习场景的时空动态，并实现更准确的未来Occupancy预测。

**技术框架**：该方法的整体框架包括以下几个主要步骤：首先，从原始图像中提取特征；然后，利用Transformer架构对这些特征进行处理，以学习场景的时空依赖关系；最后，基于学习到的特征，预测未来多帧的稀疏Occupancy。该框架避免了中间的BEV投影步骤，直接在原始图像特征上进行操作。

**关键创新**：该方法最重要的技术创新点在于采用了稀疏Occupancy表征，并将其与Transformer架构相结合。与现有方法相比，该方法避免了离散tokenization和BEV投影，从而能够更有效地表征和预测未来场景的Occupancy。这种稀疏表征允许模型关注场景中最重要的区域，从而提高了预测的准确性和效率。

**关键设计**：在具体实现上，该方法使用了基于注意力机制的Transformer架构，该架构能够有效地捕获时空依赖关系。此外，该方法还设计了一种损失函数，用于训练模型预测未来Occupancy。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

该方法在nuScenes基准测试中取得了最先进的性能，显著优于现有的方法。具体来说，在1-3秒的Occupancy预测任务中，该方法实现了明显的性能提升，证明了其在场景动态理解和未来预测方面的优越性。实验结果表明，该方法在任意未来轨迹条件下都能保持高精度，体现了其鲁棒性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能监控等领域。通过预测未来场景的Occupancy，可以帮助自动驾驶车辆更好地规划行驶路径，提高安全性；机器人可以更好地理解周围环境，从而实现更智能的导航；智能监控系统可以预测潜在的危险情况，从而提高预警能力。该研究具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> This paper introduces a novel architecture for trajectory-conditioned forecasting of future 3D scene occupancy. In contrast to methods that rely on variational autoencoders (VAEs) to generate discrete occupancy tokens, which inherently limit representational capacity, our approach predicts multi-frame future occupancy in an end-to-end manner directly from raw image features. Inspired by the success of attention-based transformer architectures in foundational vision and language models such as GPT and VGGT, we employ a sparse occupancy representation that bypasses the intermediate bird's eye view (BEV) projection and its explicit geometric priors. This design allows the transformer to capture spatiotemporal dependencies more effectively. By avoiding both the finite-capacity constraint of discrete tokenization and the structural limitations of BEV representations, our method achieves state-of-the-art performance on the nuScenes benchmark for 1-3 second occupancy forecasting, outperforming existing approaches by a significant margin. Furthermore, it demonstrates robust scene dynamics understanding, consistently delivering high accuracy under arbitrary future trajectory conditioning.

