---
layout: default
title: "Focus Through Motion: RGB-Event Collaborative Token Sparsification for Efficient Object Detection"
---

# Focus Through Motion: RGB-Event Collaborative Token Sparsification for Efficient Object Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03872" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03872v1</a>
  <a href="https://arxiv.org/pdf/2509.03872.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03872v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03872v1', 'Focus Through Motion: RGB-Event Collaborative Token Sparsification for Efficient Object Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nan Yang, Yang Wang, Zhanwen Liu, Yuchao Dai, Yang Liu, Xiangmo Zhao

**分类**: cs.CV

**发布日期**: 2025-09-04

**🔗 代码/项目**: [GITHUB](https://github.com/Zizzzzzzz/FocusMamba)

---

## 💡 一句话要点

**提出FocusMamba，通过RGB-Event协同Token稀疏化实现高效目标检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `RGB-Event` `目标检测` `多模态融合` `Token稀疏化` `事件相机`

## 📋 核心要点

1. 现有RGB-Event检测方法对低信息区域统一处理，导致计算冗余和性能瓶颈。
2. FocusMamba通过事件引导的多模态稀疏化策略，自适应地丢弃低信息区域，提升效率。
3. 实验表明，FocusMamba在DSEC-Det和PKU-DAVIS-SOD数据集上，精度和效率均优于现有方法。

## 📝 摘要（中文）

现有的RGB-Event检测方法在特征提取和融合过程中，对两种模态中的低信息区域（图像中的背景和事件数据中的非事件区域）进行统一处理，导致计算成本高昂且性能欠佳。为了减少特征提取过程中的计算冗余，研究人员分别针对图像和事件模态提出了token稀疏化方法。然而，这些方法采用固定数量或阈值进行token选择，阻碍了信息量丰富的token的保留，尤其是在处理复杂度不同的样本时。为了在精度和效率之间取得更好的平衡，本文提出了FocusMamba，它执行多模态特征的自适应协同稀疏化，并有效地整合互补信息。具体而言，设计了一种事件引导的多模态稀疏化（EGMS）策略，通过利用事件相机感知的场景内容变化来识别和自适应地丢弃每种模态内的低信息区域。基于稀疏化结果，提出了一种跨模态焦点融合（CMFF）模块，以有效地捕获和整合来自两种模态的互补特征。在DSEC-Det和PKU-DAVIS-SOD数据集上的实验表明，与现有方法相比，该方法在准确性和效率方面均实现了卓越的性能。

## 🔬 方法详解

**问题定义**：现有的RGB-Event目标检测方法在处理图像和事件数据时，对所有区域同等对待，即使是背景区域或者没有事件发生的区域，也会进行大量的特征提取和计算，导致计算资源的浪费。此外，固定数量或阈值的token稀疏化方法无法适应不同复杂度的场景，可能丢失关键信息。

**核心思路**：FocusMamba的核心思路是利用事件相机对场景变化的感知能力，引导图像和事件数据的特征稀疏化，自适应地去除低信息区域的token，从而减少计算量，并保留重要的互补信息。通过跨模态融合，进一步提升检测性能。

**技术框架**：FocusMamba主要包含两个核心模块：事件引导的多模态稀疏化（EGMS）和跨模态焦点融合（CMFF）。首先，EGMS模块利用事件数据动态地识别图像和事件数据中的低信息区域，并进行稀疏化处理。然后，CMFF模块将稀疏化后的图像和事件特征进行融合，提取互补信息，用于最终的目标检测。

**关键创新**：该方法最重要的创新点在于事件引导的多模态自适应稀疏化。不同于以往的固定稀疏化策略，FocusMamba能够根据场景的动态变化，自适应地调整稀疏化的程度，从而更好地平衡计算效率和检测精度。此外，跨模态焦点融合模块能够有效地整合两种模态的互补信息。

**关键设计**：EGMS模块的设计关键在于如何有效地利用事件数据来指导图像和事件数据的稀疏化。具体实现细节未知，但可以推测可能使用了注意力机制或者其他相关技术。CMFF模块的设计关键在于如何有效地融合两种模态的特征，可能采用了跨模态注意力机制或者其他特征融合方法。具体的参数设置、损失函数和网络结构等技术细节在论文中应该有详细描述，但此处未知。

## 📊 实验亮点

FocusMamba在DSEC-Det和PKU-DAVIS-SOD数据集上取得了显著的性能提升。具体的数据指标未知，但摘要中明确指出，与现有方法相比，FocusMamba在准确性和效率方面均实现了卓越的性能。这意味着该方法在实际应用中能够更好地平衡检测精度和计算资源消耗。

## 🎯 应用场景

FocusMamba在自动驾驶、机器人导航、智能监控等领域具有广泛的应用前景。通过高效地处理RGB-Event数据，该方法能够提升目标检测的速度和精度，尤其是在高动态范围和光照条件不佳的环境下，具有重要的实际价值。未来，该方法可以进一步扩展到其他多模态融合任务中。

## 📄 摘要（原文）

> Existing RGB-Event detection methods process the low-information regions of both modalities (background in images and non-event regions in event data) uniformly during feature extraction and fusion, resulting in high computational costs and suboptimal performance. To mitigate the computational redundancy during feature extraction, researchers have respectively proposed token sparsification methods for the image and event modalities. However, these methods employ a fixed number or threshold for token selection, hindering the retention of informative tokens for samples with varying complexity. To achieve a better balance between accuracy and efficiency, we propose FocusMamba, which performs adaptive collaborative sparsification of multimodal features and efficiently integrates complementary information. Specifically, an Event-Guided Multimodal Sparsification (EGMS) strategy is designed to identify and adaptively discard low-information regions within each modality by leveraging scene content changes perceived by the event camera. Based on the sparsification results, a Cross-Modality Focus Fusion (CMFF) module is proposed to effectively capture and integrate complementary features from both modalities. Experiments on the DSEC-Det and PKU-DAVIS-SOD datasets demonstrate that the proposed method achieves superior performance in both accuracy and efficiency compared to existing methods. The code will be available at https://github.com/Zizzzzzzz/FocusMamba.

