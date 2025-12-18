---
layout: default
title: VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation
---

# VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15530" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15530v4</a>
  <a href="https://arxiv.org/pdf/2510.15530.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15530v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15530v4', 'VO-DP: Semantic-Geometric Adaptive Diffusion Policy for Vision-Only Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zehao Ni, Yonghao He, Lingfeng Qian, Jilei Mao, Fa Fu, Wei Sui, Hu Su, Junran Peng, Zhipeng Wang, Bin He

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-10-17 (更新: 2025-11-03)

---

## 💡 一句话要点

**提出VO-DP：一种基于视觉的语义-几何自适应扩散策略，用于机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `视觉策略学习` `扩散模型` `语义特征` `几何特征` `预训练模型` `模仿学习`

## 📋 核心要点

1. 现有的基于视觉运动的扩散策略学习方法主要依赖点云输入，缺乏对仅视觉解决方案的深入探索。
2. VO-DP利用预训练视觉基础模型，融合语义和几何特征，实现高效的视觉机器人操作策略学习。
3. 实验表明，VO-DP在模拟和真实世界任务中均优于基线方法，并在不同条件下表现出高度的鲁棒性。

## 📝 摘要（中文）

本文提出了一种基于视觉的机器人操作扩散策略学习方法(VO-DP)，该方法利用预训练的视觉基础模型来实现语义和几何特征的有效融合。VO-DP利用VGGT的中间特征，结合DINOv2的语义特征和交替注意力块的几何特征。通过交叉注意力融合特征，并使用CNN进行空间压缩，形成策略头的输入。大量实验表明，VO-DP不仅显著优于仅基于视觉的基线DP，而且相对于基于点云的方法DP3表现出明显的性能趋势：在模拟任务中，VO-DP的平均成功率为64.6%，与DP3的64.0%相当，远高于DP的34.8%；在真实世界任务中，VO-DP达到87.9%，显著优于DP3的67.5%和DP的11.2%。进一步的鲁棒性评估证实，VO-DP在颜色、大小、背景和光照等不同条件下保持高度稳定。最后，我们开源了一个机器人操作训练库，该库基于Accelerate，支持多机多GPU并行训练以及混合精度训练，兼容DP、DP3和VO-DP等视觉运动策略，并支持RoboTwin模拟器。

## 🔬 方法详解

**问题定义**：论文旨在解决仅使用视觉信息进行机器人操作任务的问题。现有方法通常依赖于点云数据，而仅使用视觉信息的方案缺乏对语义和几何信息的有效融合，导致性能受限。

**核心思路**：VO-DP的核心思路是利用预训练的视觉基础模型提取图像中的语义和几何特征，并通过自适应的方式进行融合，从而提升视觉机器人操作策略的性能。通过结合不同模型的优势，弥补了仅使用单一视觉信息源的不足。

**技术框架**：VO-DP的整体框架包括以下几个主要模块：1) 特征提取：使用VGGT提取图像的中间特征，DINOv2提取语义特征，交替注意力块提取几何特征。2) 特征融合：通过交叉注意力机制将语义和几何特征进行融合。3) 特征压缩：使用CNN对融合后的特征进行空间压缩。4) 策略头：将压缩后的特征输入策略头，生成机器人动作。

**关键创新**：VO-DP的关键创新在于语义和几何特征的自适应融合。通过交叉注意力机制，模型可以根据任务需求动态地调整语义和几何特征的权重，从而实现更有效的特征表示。此外，使用预训练的视觉基础模型可以减少对大量标注数据的依赖。

**关键设计**：VO-DP的关键设计包括：1) 使用VGGT的中间特征，以保留更多的空间信息。2) 使用DINOv2提取语义特征，利用其强大的语义表示能力。3) 使用交替注意力块提取几何特征，捕捉图像中的结构信息。4) 通过交叉注意力机制融合特征，实现自适应的特征表示。5) 使用CNN进行空间压缩，减少计算量。

## 📊 实验亮点

VO-DP在模拟任务中取得了与基于点云的方法DP3相当的性能（64.6% vs 64.0%），远高于仅基于视觉的基线DP（34.8%）。更重要的是，在真实世界任务中，VO-DP的成功率达到了87.9%，显著优于DP3（67.5%）和DP（11.2%）。此外，VO-DP在颜色、大小、背景和光照等不同条件下表现出高度的鲁棒性。

## 🎯 应用场景

VO-DP具有广泛的应用前景，例如在家庭服务机器人、工业自动化、医疗辅助机器人等领域。该方法可以使机器人仅通过视觉信息就能完成复杂的操作任务，降低了对传感器硬件的要求，并提高了机器人的灵活性和适应性。未来，VO-DP有望应用于更复杂的环境和任务中，例如在未知环境中进行物体抓取和操作。

## 📄 摘要（原文）

> In the context of imitation learning, visuomotor-based diffusion policy learning is one of the main directions in robotic manipulation. Most of these approaches rely on point clouds as observation inputs and construct scene representations through point clouds feature learning, which enables them to achieve remarkable accuracy. However, the existing literature lacks an in-depth exploration of vision-only solutions that have significant potential. In this paper, we propose a Vision-Only and single-view Diffusion Policy learning method (VO-DP) that leverages pretrained visual foundation models to achieve effective fusion of semantic and geometric features. We utilize intermediate features from VGGT incorporating semantic features from DINOv2 and geometric features from Alternating Attention blocks. Features are fused via cross-attention and spatially compressed with a CNN to form the input to the policy head. Extensive experiments demonstrate that VO-DP not only outperforms the vision-only baseline DP significantly but also exhibits distinct performance trends against the point cloud-based method DP3: in simulation tasks, VO-DP achieves an average success rate of 64.6% on par with DP3 64.0% and far higher than DP 34.8%, while in real-world tasks, it reaches 87.9%, outperforming both DP3 67.5% and DP 11.2% by a notable margin. Further robustness evaluations confirm that VO-DP remains highly stable under varying conditions including color, size, background, and lighting. Lastly, we open-source a training library for robotic manipulation. Built on Accelerate, this library supports multi-machine and multi-GPU parallel training, as well as mixed precision training. It is compatible with visuomotor policies such as DP, DP3 and VO-DP, and also supports the RoboTwin simulator.

