---
layout: default
title: CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation
---

# CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03992" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03992v1</a>
  <a href="https://arxiv.org/pdf/2511.03992.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03992v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03992v1', 'CaRF: Enhancing Multi-View Consistency in Referring 3D Gaussian Splatting Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuwen Tao, Kanglei Zhou, Xin Tan, Yuan Xie

**分类**: cs.CV

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**CaRF：通过增强多视角一致性改进Referring 3D高斯溅射分割**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `Referring 3D分割` `高斯溅射` `多视角一致性` `相机感知` `跨模态对齐`

## 📋 核心要点

1. 现有Referring 3D高斯溅射分割方法依赖2D渲染伪监督，导致视角不一致，限制了分割性能。
2. CaRF通过引入相机感知的高斯场编码和训练时配对视角监督，直接在3D高斯空间中实现多视角一致性。
3. 实验表明，CaRF在多个数据集上显著提升了Referring 3D分割的mIoU，优于现有技术水平。

## 📝 摘要（中文）

Referring 3D Gaussian Splatting Segmentation (R3DGS) 旨在解析自由形式的语言表达，并在高斯场中定位相应的 3D 区域。尽管最近的研究在语言和 3D 几何之间引入了跨模态对齐，但由于现有流程依赖于 2D 渲染的伪监督和特定视角的特征学习，因此仍然难以实现跨视角一致性。本文提出了 Camera Aware Referring Field (CaRF)，这是一个完全可微的框架，直接在高斯 3D 空间中运行并实现多视角一致性。具体来说，CaRF 引入了 Gaussian Field Camera Encoding (GFCE)，它将相机几何信息融入高斯文本交互中，以显式地建模视角相关的变化并增强几何推理。在此基础上，提出了 In Training Paired View Supervision (ITPVS)，用于在训练期间对齐校准视角之间的每个高斯逻辑值，从而有效地缓解单视角过拟合，并暴露视角间的差异以进行优化。在三个代表性基准上的大量实验表明，CaRF 在 Ref LERF、LERF OVS 和 3D OVS 数据集上，相对于最先进的方法，平均 mIoU 分别提高了 16.8%、4.3% 和 2.0%。此外，这项工作促进了更可靠和视角一致的 3D 场景理解，并为具身 AI、AR/VR 交互和自主感知带来了潜在的好处。

## 🔬 方法详解

**问题定义**：现有Referring 3D高斯溅射分割方法在处理跨视角一致性方面存在困难。它们依赖于从2D渲染图像获得的伪标签进行训练，这导致模型学习到视角相关的特征，从而在不同视角下产生不一致的分割结果。这种不一致性限制了模型在实际应用中的可靠性。

**核心思路**：CaRF的核心思路是在3D高斯空间中直接进行推理和学习，避免依赖2D渲染的伪标签。通过引入相机感知的编码方式，将相机几何信息融入到高斯特征中，从而显式地建模视角相关的变化。此外，通过在训练时对齐不同视角下的高斯特征，进一步增强模型的多视角一致性。

**技术框架**：CaRF框架主要包含两个核心模块：Gaussian Field Camera Encoding (GFCE) 和 In Training Paired View Supervision (ITPVS)。GFCE模块将相机参数（如位置和方向）编码到每个高斯粒子的特征中，使得模型能够感知视角信息。ITPVS模块在训练过程中，对来自不同视角的同一高斯粒子的预测结果进行对齐，从而增强模型的多视角一致性。整体流程是，首先使用GFCE对高斯特征进行编码，然后使用ITPVS进行训练，最终得到具有多视角一致性的分割结果。

**关键创新**：CaRF的关键创新在于其完全在3D高斯空间中进行推理和学习，避免了对2D渲染的依赖。GFCE模块显式地建模了视角相关的变化，使得模型能够更好地理解3D场景的几何信息。ITPVS模块通过对齐不同视角的预测结果，有效地增强了模型的多视角一致性。与现有方法相比，CaRF能够更准确地分割3D场景中的目标物体，并且在不同视角下具有更高的鲁棒性。

**关键设计**：GFCE模块使用一个小型神经网络将相机参数编码为高斯特征的附加向量。ITPVS模块使用交叉熵损失函数来对齐不同视角下的高斯逻辑值。具体来说，对于每个高斯粒子，从两个不同的视角渲染得到两个逻辑值向量，然后计算这两个向量之间的交叉熵损失，并将其作为训练目标之一。此外，论文还使用了标准的高斯溅射渲染技术和语言编码器来提取文本特征。

## 📊 实验亮点

CaRF在Ref LERF、LERF OVS和3D OVS三个数据集上进行了评估，实验结果表明，CaRF显著优于现有方法。具体来说，CaRF在Ref LERF数据集上取得了16.8%的mIoU提升，在LERF OVS数据集上取得了4.3%的mIoU提升，在3D OVS数据集上取得了2.0%的mIoU提升。这些结果表明，CaRF能够有效地提高Referring 3D分割的准确性和鲁棒性。

## 🎯 应用场景

CaRF在具身AI、AR/VR交互和自主感知等领域具有广泛的应用前景。例如，在机器人导航中，机器人可以利用CaRF来理解人类的指令，并在3D环境中定位目标物体。在AR/VR应用中，CaRF可以用于增强用户与虚拟环境的交互体验，例如，用户可以通过语音指令来操作虚拟物体。在自动驾驶中，CaRF可以用于识别和分割道路上的交通标志和行人，从而提高驾驶安全性。

## 📄 摘要（原文）

> Referring 3D Gaussian Splatting Segmentation (R3DGS) aims to interpret free-form language expressions and localize the corresponding 3D regions in Gaussian fields. While recent advances have introduced cross-modal alignment between language and 3D geometry, existing pipelines still struggle with cross-view consistency due to their reliance on 2D rendered pseudo supervision and view specific feature learning. In this work, we present Camera Aware Referring Field (CaRF), a fully differentiable framework that operates directly in the 3D Gaussian space and achieves multi view consistency. Specifically, CaRF introduces Gaussian Field Camera Encoding (GFCE), which incorporates camera geometry into Gaussian text interactions to explicitly model view dependent variations and enhance geometric reasoning. Building on this, In Training Paired View Supervision (ITPVS) is proposed to align per Gaussian logits across calibrated views during training, effectively mitigating single view overfitting and exposing inter view discrepancies for optimization. Extensive experiments on three representative benchmarks demonstrate that CaRF achieves average improvements of 16.8%, 4.3%, and 2.0% in mIoU over state of the art methods on the Ref LERF, LERF OVS, and 3D OVS datasets, respectively. Moreover, this work promotes more reliable and view consistent 3D scene understanding, with potential benefits for embodied AI, AR/VR interaction, and autonomous perception.

