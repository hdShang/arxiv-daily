---
layout: default
title: "StruMamba3D: Exploring Structural Mamba for Self-supervised Point Cloud Representation Learning"
---

# StruMamba3D: Exploring Structural Mamba for Self-supervised Point Cloud Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21541" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21541v3</a>
  <a href="https://arxiv.org/pdf/2506.21541.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21541v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21541v3', 'StruMamba3D: Exploring Structural Mamba for Self-supervised Point Cloud Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chuxin Wang, Yixin Zha, Wenfei Yang, Tianzhu Zhang

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-07-30)

**备注**: Accepted by ICCV 2025, website: https://chuxwa.github.io/project_StruMamba3D/

---

## 💡 一句话要点

**提出StruMamba3D以解决SSM在点云表示学习中的局限性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `点云表示学习` `自监督学习` `状态空间模型` `空间状态` `结构建模` `深度学习` `机器人视觉`

## 📋 核心要点

1. 现有Mamba方法在点云表示学习中存在邻接关系破坏和长序列记忆保持不足的问题。
2. StruMamba3D通过设计空间状态和状态更新策略，增强了SSM的结构建模能力，保持了点之间的空间依赖性。
3. 实验结果显示，该方法在多个下游任务中表现优异，尤其在ModelNet40和ScanObjectNN上取得了显著的准确率提升。

## 📝 摘要（中文）

近年来，基于Mamba的方法在点云表示学习中表现出色，利用状态空间模型（SSM）具备高效的上下文建模能力和线性复杂度。然而，这些方法仍面临两个关键问题：在SSM处理过程中破坏了3D点的邻接关系，以及在下游任务中输入长度增加时无法保持长序列记忆。为了解决这些问题，我们提出了StruMamba3D，这是一种新颖的自监督点云表示学习范式。该方法设计了空间状态，作为代理以保持点之间的空间依赖性，并通过状态更新策略和轻量卷积增强SSM，促进空间状态之间的交互。此外，我们引入序列长度自适应策略，降低了预训练Mamba模型对输入长度变化的敏感性。实验结果表明，该方法在四个下游任务中表现优异，并在ModelNet40上达到了95.1%的SOTA准确率，在ScanObjectNN的最具挑战性分割上达到了92.75%的准确率，且无需投票策略。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有Mamba方法在点云表示学习中存在的两个主要问题：一是SSM处理过程中破坏了3D点的邻接关系，二是在输入长度增加时无法有效保持长序列记忆。

**核心思路**：我们提出StruMamba3D，通过引入空间状态作为代理来保持点之间的空间依赖性，并采用状态更新策略和轻量卷积来增强SSM的结构建模能力，从而有效解决上述问题。

**技术框架**：StruMamba3D的整体架构包括空间状态的设计、状态更新策略的实施以及轻量卷积的集成。首先，通过空间状态来捕捉点云中点之间的空间关系；其次，利用状态更新策略来优化信息传递；最后，轻量卷积用于促进空间状态之间的交互。

**关键创新**：本研究的主要创新在于引入空间状态和状态更新策略，这与传统的Mamba方法相比，显著提高了对点云结构的建模能力，并降低了对输入长度变化的敏感性。

**关键设计**：在技术细节上，我们设计了适应不同输入长度的序列长度自适应策略，并在损失函数和网络结构上进行了优化，以确保模型在不同任务中的稳定性和准确性。

## 📊 实验亮点

在实验中，StruMamba3D在ModelNet40数据集上达到了95.1%的准确率，在ScanObjectNN的最具挑战性分割上达到了92.75%的准确率，均为当前最优性能，且在这些任务中无需使用投票策略，显示出其卓越的性能和稳定性。

## 🎯 应用场景

该研究在自动驾驶、机器人导航和三维重建等领域具有广泛的应用潜力。通过提高点云表示学习的准确性和效率，StruMamba3D能够为这些领域提供更为可靠的支持，推动相关技术的发展和应用。未来，该方法还可能扩展到其他三维数据处理任务中，进一步提升其实际价值。

## 📄 摘要（原文）

> Recently, Mamba-based methods have demonstrated impressive performance in point cloud representation learning by leveraging State Space Model (SSM) with the efficient context modeling ability and linear complexity. However, these methods still face two key issues that limit the potential of SSM: Destroying the adjacency of 3D points during SSM processing and failing to retain long-sequence memory as the input length increases in downstream tasks. To address these issues, we propose StruMamba3D, a novel paradigm for self-supervised point cloud representation learning. It enjoys several merits. First, we design spatial states and use them as proxies to preserve spatial dependencies among points. Second, we enhance the SSM with a state-wise update strategy and incorporate a lightweight convolution to facilitate interactions between spatial states for efficient structure modeling. Third, our method reduces the sensitivity of pre-trained Mamba-based models to varying input lengths by introducing a sequence length-adaptive strategy. Experimental results across four downstream tasks showcase the superior performance of our method. In addition, our method attains the SOTA 95.1% accuracy on ModelNet40 and 92.75% accuracy on the most challenging split of ScanObjectNN without voting strategy.

