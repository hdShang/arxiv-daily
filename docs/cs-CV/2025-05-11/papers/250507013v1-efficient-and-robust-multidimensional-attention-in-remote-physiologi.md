---
layout: default
title: Efficient and Robust Multidimensional Attention in Remote Physiological Sensing through Target Signal Constrained Factorization
---

# Efficient and Robust Multidimensional Attention in Remote Physiological Sensing through Target Signal Constrained Factorization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07013" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07013v1</a>
  <a href="https://arxiv.org/pdf/2505.07013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07013v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07013v1', 'Efficient and Robust Multidimensional Attention in Remote Physiological Sensing through Target Signal Constrained Factorization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jitesh Joshi, Youngjun Cho

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-11

**备注**: 25 pages, 6 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://physiologicailab.github.io/mmrphys-live)

---

## 💡 一句话要点

**提出目标信号约束因子分解以解决远程生理信号监测的鲁棒性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `远程生理监测` `目标信号约束` `因子分解` `多模态输入` `深度学习` `实时应用` `鲁棒性评估`

## 📋 核心要点

1. 现有深度学习方法在远程生理信号监测中对领域转移的鲁棒性不足，影响实际应用效果。
2. 提出目标信号约束因子分解模块（TSFM），通过生理信号特征约束提升特征提取精度，构建MMRPhys架构。
3. 在五个基准数据集上进行交叉评估，MMRPhys显著提高了rPPG和rRSP估计的鲁棒性，推理延迟低，适合实时应用。

## 📝 摘要（中文）

基于摄像头的远程生理监测技术在非侵入式生命体征监测方面具有变革潜力。尽管深度学习方法在视频数据中提取生理信号方面取得了进展，但现有方法在应对领域转移时的鲁棒性评估不足。本文提出了目标信号约束因子分解模块（TSFM），通过将生理信号特征作为因子约束，提升特征提取的精确度。基于此，我们设计了MMRPhys，一个高效的双支路3D-CNN架构，能够同时从多模态RGB和热视频输入中估计光电容积脉搏（rPPG）和呼吸信号（rRSP）。通过在五个基准数据集上的全面交叉数据集评估，MMRPhys与TSFM在领域转移的鲁棒性上显著超越了现有方法，同时保持适合实时应用的低推理延迟。

## 🔬 方法详解

**问题定义**：本文旨在解决现有远程生理信号监测方法在面对领域转移（如环境变化、摄像头规格等）时的鲁棒性不足问题。现有方法未能充分评估其在真实场景中的表现，限制了其应用潜力。

**核心思路**：论文提出目标信号约束因子分解模块（TSFM），通过将生理信号特征作为因子约束，提升特征提取的精确度。这种设计使得模型能够更好地适应不同的环境和条件变化。

**技术框架**：整体架构为MMRPhys，一个双支路3D-CNN模型，能够同时处理多模态输入（RGB和热视频），并进行rPPG和rRSP的多任务估计。模型通过TSFM模块增强特征提取能力，确保在不同条件下的鲁棒性。

**关键创新**：最重要的技术创新点在于引入了TSFM模块，该模块通过生理信号特征的约束实现了更精确的特征提取，与现有方法相比，显著提高了模型在领域转移中的鲁棒性。

**关键设计**：模型采用双支路结构，分别处理RGB和热视频输入，使用特定的损失函数优化rPPG和rRSP的估计精度。网络结构经过精心设计，以确保在保持低推理延迟的同时，提升模型的整体性能。

## 📊 实验亮点

实验结果表明，MMRPhys与TSFM在五个基准数据集上的表现显著优于现有最先进方法，尤其在领域转移的鲁棒性方面，rPPG和rRSP的估计精度均有显著提升，推理延迟保持在最低水平，适合实时应用。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康监测和人机交互等场景，能够实现非侵入式的生命体征监测，提升用户体验和健康管理的效率。未来，该技术有望在智能设备和可穿戴设备中得到广泛应用，推动个性化医疗的发展。

## 📄 摘要（原文）

> Remote physiological sensing using camera-based technologies offers transformative potential for non-invasive vital sign monitoring across healthcare and human-computer interaction domains. Although deep learning approaches have advanced the extraction of physiological signals from video data, existing methods have not been sufficiently assessed for their robustness to domain shifts. These shifts in remote physiological sensing include variations in ambient conditions, camera specifications, head movements, facial poses, and physiological states which often impact real-world performance significantly. Cross-dataset evaluation provides an objective measure to assess generalization capabilities across these domain shifts. We introduce Target Signal Constrained Factorization module (TSFM), a novel multidimensional attention mechanism that explicitly incorporates physiological signal characteristics as factorization constraints, allowing more precise feature extraction. Building on this innovation, we present MMRPhys, an efficient dual-branch 3D-CNN architecture designed for simultaneous multitask estimation of photoplethysmography (rPPG) and respiratory (rRSP) signals from multimodal RGB and thermal video inputs. Through comprehensive cross-dataset evaluation on five benchmark datasets, we demonstrate that MMRPhys with TSFM significantly outperforms state-of-the-art methods in generalization across domain shifts for rPPG and rRSP estimation, while maintaining a minimal inference latency suitable for real-time applications. Our approach establishes new benchmarks for robust multitask and multimodal physiological sensing and offers a computationally efficient framework for practical deployment in unconstrained environments. The web browser-based application featuring on-device real-time inference of MMRPhys model is available at https://physiologicailab.github.io/mmrphys-live

