---
layout: default
title: "DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method"
---

# DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17054" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17054v3</a>
  <a href="https://arxiv.org/pdf/2508.17054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17054v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17054v3', 'DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingwen Zhang, Xiaomeng Zhu, Yushan Zhang, Yixi Cai, Olov Andersson, Patric Jensfelt

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-23 (更新: 2025-12-22)

**备注**: NeurIPS 2025 Spotlight, 18 pages (10 main pages + 8 supp materail), 11 figures, code at https://github.com/Kin-Zhang/DeltaFlow

**🔗 代码/项目**: [GITHUB](https://github.com/Kin-Zhang/DeltaFlow)

---

## 💡 一句话要点

**提出DeltaFlow以高效解决多帧场景流估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `场景流估计` `多帧推理` `运动捕捉` `类别平衡损失` `实例一致性损失` `自动驾驶` `机器人导航`

## 📋 核心要点

1. 现有的场景流估计方法主要依赖于两帧图像，未能充分利用时间信息，导致性能受限。
2. 本文提出的DeltaFlow通过$Δ$方案高效提取多帧时间特征，显著降低计算成本，提升场景流估计的准确性。
3. 实验结果表明，DeltaFlow在多个数据集上实现了22%的误差降低和2倍的推理速度提升，展现出优越的性能和泛化能力。

## 📝 摘要（中文）

现有的场景流估计方法主要集中在两帧之间的信息，忽视了时间域中的宝贵信息。尽管近期的研究趋势向多帧推理转变，但随着帧数的增加，计算成本迅速上升。为此，本文提出了DeltaFlow（$Δ$Flow），一个轻量级的3D框架，通过$Δ$方案捕捉运动线索，以最小的计算成本提取时间特征。此外，场景流估计还面临类别不平衡和运动不一致等挑战。为解决这些问题，本文引入了类别平衡损失和实例一致性损失，提升了流的准确性。在Argoverse 2、Waymo和nuScenes数据集上的广泛评估表明，$Δ$Flow在性能上达到了最先进水平，误差降低了22%，推理速度提高了2倍，同时展现出强大的跨领域泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有场景流估计方法在处理多帧输入时的计算成本过高和信息利用不足的问题。现有方法多依赖于两帧图像，未能有效利用时间域信息，导致性能受限。

**核心思路**：DeltaFlow通过引入$Δ$方案，能够在不增加计算负担的情况下，提取多帧的时间特征，从而更高效地捕捉运动信息。该设计旨在平衡计算效率与估计准确性。

**技术框架**：DeltaFlow的整体架构包括多个模块，首先通过$Δ$方案提取时间特征，然后应用类别平衡损失和实例一致性损失来优化学习过程，最终输出场景流估计结果。

**关键创新**：本文的主要创新在于引入了类别平衡损失和实例一致性损失，这两种损失函数有效解决了类别不平衡和运动不一致的问题，显著提升了流的估计精度。

**关键设计**：在网络结构上，DeltaFlow采用了轻量级设计，确保在处理多帧数据时保持较低的计算成本。同时，损失函数的设计使得模型在训练过程中能够更好地学习到稀有类别的特征，提高了整体性能。

## 📊 实验亮点

在多个数据集上的实验结果显示，DeltaFlow相比于下一最佳的多帧监督方法，误差降低了22%，推理速度提高了2倍，展现出卓越的性能和强大的跨领域泛化能力，标志着场景流估计领域的一次重要进展。

## 🎯 应用场景

DeltaFlow的研究成果在自动驾驶、机器人导航和视频分析等领域具有广泛的应用潜力。通过高效的场景流估计，能够提升机器对动态环境的理解能力，从而增强智能系统的决策能力和反应速度，推动相关技术的发展。

## 📄 摘要（原文）

> Previous dominant methods for scene flow estimation focus mainly on input from two consecutive frames, neglecting valuable information in the temporal domain. While recent trends shift towards multi-frame reasoning, they suffer from rapidly escalating computational costs as the number of frames grows. To leverage temporal information more efficiently, we propose DeltaFlow ($Δ$Flow), a lightweight 3D framework that captures motion cues via a $Δ$ scheme, extracting temporal features with minimal computational cost, regardless of the number of frames. Additionally, scene flow estimation faces challenges such as imbalanced object class distributions and motion inconsistency. To tackle these issues, we introduce a Category-Balanced Loss to enhance learning across underrepresented classes and an Instance Consistency Loss to enforce coherent object motion, improving flow accuracy. Extensive evaluations on the Argoverse 2, Waymo and nuScenes datasets show that $Δ$Flow achieves state-of-the-art performance with up to 22% lower error and $2\times$ faster inference compared to the next-best multi-frame supervised method, while also demonstrating a strong cross-domain generalization ability. The code is open-sourced at https://github.com/Kin-Zhang/DeltaFlow along with trained model weights.

