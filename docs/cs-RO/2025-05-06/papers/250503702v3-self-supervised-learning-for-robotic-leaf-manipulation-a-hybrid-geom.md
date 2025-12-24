---
layout: default
title: "Self-Supervised Learning for Robotic Leaf Manipulation: A Hybrid Geometric-Neural Approach"
---

# Self-Supervised Learning for Robotic Leaf Manipulation: A Hybrid Geometric-Neural Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03702" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03702v3</a>
  <a href="https://arxiv.org/pdf/2505.03702.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03702v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03702v3', 'Self-Supervised Learning for Robotic Leaf Manipulation: A Hybrid Geometric-Neural Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Srecharan Selvam

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-05-06 (更新: 2025-05-16)

**备注**: 15 pages, 9 figures

---

## 💡 一句话要点

**提出混合几何-神经方法以解决农业机器人叶片操作问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `农业机器人` `自监督学习` `混合方法` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有的农业机器人在叶片操作中面临植物形态多样性和叶片变形等挑战，导致抓取成功率低。
2. 本文提出了一种混合几何-神经的方法，通过自监督学习结合YOLOv8和RAFT-Stereo，提升叶片抓取的准确性。
3. 实验结果显示，该方法在受控环境和真实温室条件下的成功率分别达到88.0%和84.7%，显著优于现有方法。

## 📝 摘要（中文）

在农业环境中，自动化叶片操作面临植物形态多样性和叶片可变形等重大挑战。本文提出了一种新颖的混合几何-神经方法，通过自监督学习结合传统计算机视觉与神经网络，实现自主叶片抓取。该方法整合YOLOv8进行实例分割和RAFT-Stereo进行3D深度估计，以构建丰富的叶片表示，并输入到几何特征评分管道和神经细化模块（GraspPointCNN）。关键创新在于自适应的置信加权融合机制，根据预测的确定性动态平衡各方法的贡献。实验结果表明，该方法在受控环境中成功率达到88.0%，在真实温室条件下为84.7%，显著优于纯几何（75.3%）和纯神经（60.2%）方法。这项工作为农业机器人建立了一个新的范式，将领域专业知识与机器学习能力无缝集成，为完全自动化的作物监测系统奠定基础。

## 🔬 方法详解

**问题定义**：本文旨在解决农业机器人在叶片操作中面临的抓取成功率低的问题，现有方法在处理植物形态多样性和叶片变形时存在明显不足。

**核心思路**：提出一种混合几何-神经的方法，通过自监督学习将传统计算机视觉与深度学习相结合，以提高叶片抓取的准确性和鲁棒性。

**技术框架**：整体架构包括YOLOv8进行实例分割、RAFT-Stereo进行3D深度估计、几何特征评分管道和神经细化模块（GraspPointCNN），形成一个完整的叶片表示与抓取系统。

**关键创新**：引入置信加权融合机制，根据不同方法的预测确定性动态调整其贡献，显著提升了抓取的准确性和稳定性。

**关键设计**：在训练过程中，采用几何管道作为专家教师自动生成训练数据，设计了特定的损失函数以优化模型性能，同时调整了网络结构以适应不同的输入特征。

## 📊 实验亮点

实验结果显示，提出的方法在受控环境中的成功率达到88.0%，在真实温室条件下为84.7%。相比之下，纯几何方法的成功率为75.3%，纯神经方法为60.2%，表明本文方法在抓取性能上有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括农业机器人、智能温室和自动化作物监测系统。通过提高叶片操作的自动化水平，能够有效降低人工成本，提高农业生产效率，推动智能农业的发展。

## 📄 摘要（原文）

> Automating leaf manipulation in agricultural settings faces significant challenges, including the variability of plant morphologies and deformable leaves. We propose a novel hybrid geometric-neural approach for autonomous leaf grasping that combines traditional computer vision with neural networks through self-supervised learning. Our method integrates YOLOv8 for instance segmentation and RAFT-Stereo for 3D depth estimation to build rich leaf representations, which feed into both a geometric feature scoring pipeline and a neural refinement module (GraspPointCNN). The key innovation is our confidence-weighted fusion mechanism that dynamically balances the contribution of each approach based on prediction certainty. Our self-supervised framework uses the geometric pipeline as an expert teacher to automatically generate training data. Experiments demonstrate that our approach achieves an 88.0% success rate in controlled environments and 84.7% in real greenhouse conditions, significantly outperforming both purely geometric (75.3%) and neural (60.2%) methods. This work establishes a new paradigm for agricultural robotics where domain expertise is seamlessly integrated with machine learning capabilities, providing a foundation for fully automated crop monitoring systems.

