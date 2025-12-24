---
layout: default
title: "Layered Motion Fusion: Lifting Motion Segmentation to 3D in Egocentric Videos"
---

# Layered Motion Fusion: Lifting Motion Segmentation to 3D in Egocentric Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05546" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05546v2</a>
  <a href="https://arxiv.org/pdf/2506.05546.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05546v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05546v2', 'Layered Motion Fusion: Lifting Motion Segmentation to 3D in Egocentric Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vadim Tschernezki, Diane Larlus, Iro Laina, Andrea Vedaldi

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-06-22)

**备注**: Camera-ready for CVPR25

---

## 💡 一句话要点

**提出分层运动融合以解决动态视频中的运动分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `动态视频分析` `运动分割` `3D视觉` `分层辐射场` `计算机视觉` `自我中心视频` `测试时细化`

## 📋 核心要点

1. 现有的3D技术在处理动态现象时效果不佳，尤其是在移动物体的分割任务中面临挑战。
2. 本文提出通过将2D运动分割预测融合到分层辐射场中，利用测试时细化来降低数据复杂性，从而改善动态分割。
3. 实验结果表明，所提出的方法在3D模型的分割预测上显著优于传统的2D基线，展示了3D技术在动态场景分析中的潜力。

## 📝 摘要（中文）

计算机视觉主要基于2D技术，而3D视觉仍然局限于相对狭窄的应用领域。近期的研究表明，通过融合独立的2D视图并进行去噪，3D技术能够改善输出，尤其是在自我中心视频中。然而，EPIC Fields的分析显示，3D技术在动态现象研究中效果不佳，特别是在移动物体的分割上。本文提出通过将2D模型的运动分割预测融合到分层辐射场中来改善3D动态分割，并通过测试时的细化来应对长动态视频的复杂性，从而实现运动融合与细化的协同，显著提升3D模型的分割预测效果，超越2D基线。

## 🔬 方法详解

**问题定义**：本文旨在解决在动态视频中进行运动分割的挑战，现有方法在处理复杂场景时难以捕捉几何结构，导致运动线索的融合受限。

**核心思路**：通过将2D模型的运动分割预测融合到分层辐射场中，结合测试时的细化策略，聚焦于特定帧以降低数据复杂性，从而提升动态分割效果。

**技术框架**：整体架构包括两个主要模块：首先是2D运动分割模型，其次是分层辐射场的融合模块。测试时细化过程则在模型推理阶段进行，以增强对动态场景的理解。

**关键创新**：最重要的创新在于提出了分层运动融合的方法，通过将2D运动分割信息有效整合到3D模型中，克服了传统3D技术在动态现象分析中的局限性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化运动分割的准确性，并通过调整网络结构以适应长视频的复杂性，确保模型在动态场景中表现优异。

## 📊 实验亮点

实验结果显示，所提出的分层运动融合方法在3D模型的分割预测上相较于传统2D基线提升了显著的性能，具体提升幅度达到了XX%（具体数据待补充），验证了3D技术在动态现象分析中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和智能监控等场景，能够有效提升动态视频分析的准确性和效率。未来，该方法有望在机器人导航和人机交互等领域发挥重要作用，推动相关技术的发展。

## 📄 摘要（原文）

> Computer vision is largely based on 2D techniques, with 3D vision still relegated to a relatively narrow subset of applications. However, by building on recent advances in 3D models such as neural radiance fields, some authors have shown that 3D techniques can at last improve outputs extracted from independent 2D views, by fusing them into 3D and denoising them. This is particularly helpful in egocentric videos, where the camera motion is significant, but only under the assumption that the scene itself is static. In fact, as shown in the recent analysis conducted by EPIC Fields, 3D techniques are ineffective when it comes to studying dynamic phenomena, and, in particular, when segmenting moving objects. In this paper, we look into this issue in more detail. First, we propose to improve dynamic segmentation in 3D by fusing motion segmentation predictions from a 2D-based model into layered radiance fields (Layered Motion Fusion). However, the high complexity of long, dynamic videos makes it challenging to capture the underlying geometric structure, and, as a result, hinders the fusion of motion cues into the (incomplete) scene geometry. We address this issue through test-time refinement, which helps the model to focus on specific frames, thereby reducing the data complexity. This results in a synergy between motion fusion and the refinement, and in turn leads to segmentation predictions of the 3D model that surpass the 2D baseline by a large margin. This demonstrates that 3D techniques can enhance 2D analysis even for dynamic phenomena in a challenging and realistic setting.

