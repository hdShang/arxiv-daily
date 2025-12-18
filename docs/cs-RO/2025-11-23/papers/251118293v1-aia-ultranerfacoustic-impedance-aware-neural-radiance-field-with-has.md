---
layout: default
title: AIA-UltraNeRF:Acoustic-Impedance-Aware Neural Radiance Field with Hash Encodings for Robotic Ultrasound Reconstruction and Localization
---

# AIA-UltraNeRF:Acoustic-Impedance-Aware Neural Radiance Field with Hash Encodings for Robotic Ultrasound Reconstruction and Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18293" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18293v1</a>
  <a href="https://arxiv.org/pdf/2511.18293.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18293v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18293v1', 'AIA-UltraNeRF:Acoustic-Impedance-Aware Neural Radiance Field with Hash Encodings for Robotic Ultrasound Reconstruction and Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuai Zhang, Jingsong Mu, Cancan Zhao, Leiqi Tian, Zhijun Xing, Bo Ouyang, Xiang Li

**分类**: cs.RO

**发布日期**: 2025-11-23

---

## 💡 一句话要点

**AIA-UltraNeRF：声阻抗感知神经辐射场用于机器人超声重建与定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `神经辐射场` `超声成像` `声阻抗` `机器人超声` `哈希编码`

## 📋 核心要点

1. 传统NeRF方法忽略了超声成像中声阻抗的关键作用，导致重建质量受限。
2. AIA-UltraNeRF通过哈希编码对声阻抗进行建模，加速重建和推理，并利用双重监督网络进行定位。
3. 实验表明，该方法能有效表征超声图像颜色，推理速度较原始NeRF提升9.9倍。

## 📝 摘要（中文）

本文提出了一种声阻抗感知的超声神经辐射场（AIA-UltraNeRF），用于机器人超声重建和定位。现有基于NeRF的重建方法忽略了声阻抗在超声成像中的关键作用，而定位方法则面临初始姿态选择导致的局部最小值问题。该方法设计了一个机器人超声系统（RUSS），利用AIA-UltraNeRF对3D超声图的哈希编码空间坐标进行连续函数建模，从而在无需密集采样的情况下存储声阻抗，加速了重建和推理速度。此外，提出了一个双重监督网络，利用教师和学生模型对重建地图渲染的超声图像进行哈希编码。AIA-UltraNeRF无需再次渲染图像即可检索最相似的哈希值，为定位提供离线初始图像位置。所开发的RUSS具有球形遥控中心运动机制，可实现独立于操作者的扫描模式。在体模和人体受试者上的实验结果表明，声阻抗能有效地隐式表征超声图像的颜色，AIA-UltraNeRF实现了重建和定位，推理速度比原始NeRF快9.9倍。

## 🔬 方法详解

**问题定义**：现有的基于NeRF的超声重建方法忽略了声阻抗这一重要物理属性，导致重建质量不高。同时，超声图像的定位方法容易陷入局部最小值，影响定位精度和效率。因此，需要一种能够有效利用声阻抗信息，并能快速准确进行超声图像重建和定位的方法。

**核心思路**：本文的核心思路是将声阻抗信息融入到NeRF框架中，通过对空间坐标进行哈希编码，隐式地学习声阻抗与超声图像之间的关系。同时，利用双重监督网络，通过教师-学生模型进行哈希编码的训练，从而实现快速的图像检索和定位。这样设计的目的是为了充分利用超声图像的物理特性，提高重建和定位的精度和效率。

**技术框架**：AIA-UltraNeRF的整体框架包括三个主要部分：1) 机器人超声系统（RUSS），用于获取超声图像数据；2) 基于哈希编码的NeRF重建模块，用于重建3D超声图，并存储声阻抗信息；3) 双重监督网络，用于对渲染的超声图像进行哈希编码，并进行图像检索和定位。RUSS负责数据采集，NeRF模块负责重建，双重监督网络负责定位。

**关键创新**：该方法最重要的技术创新点在于将声阻抗信息融入到NeRF框架中，并利用哈希编码进行高效的存储和检索。与现有方法相比，AIA-UltraNeRF能够更好地利用超声图像的物理特性，从而提高重建和定位的精度和效率。此外，双重监督网络的引入也为图像检索和定位提供了新的思路。

**关键设计**：AIA-UltraNeRF的关键设计包括：1) 使用哈希编码对空间坐标进行编码，从而实现高效的声阻抗存储和检索；2) 设计双重监督网络，利用教师模型和学生模型进行哈希编码的训练，从而提高图像检索的准确性；3) 采用球形遥控中心运动机制的RUSS，实现独立于操作者的扫描模式。具体的损失函数和网络结构等细节未在摘要中详细描述，属于未知信息。

## 📊 实验亮点

AIA-UltraNeRF在体模和人体受试者上的实验结果表明，该方法能够有效地利用声阻抗信息，隐式地表征超声图像的颜色。与原始NeRF相比，AIA-UltraNeRF在重建和定位方面的推理速度提高了9.9倍，证明了其高效性和实用性。这些实验结果验证了AIA-UltraNeRF在超声重建和定位方面的优势。

## 🎯 应用场景

AIA-UltraNeRF在医学影像领域具有广泛的应用前景，可用于辅助医生进行疾病诊断、手术规划和介入治疗。通过高精度、快速的超声重建和定位，可以提高诊断的准确性和效率，减少手术风险，并为患者提供更好的医疗服务。此外，该技术还可以应用于机器人辅助超声检查，实现远程医疗和智能化诊断。

## 📄 摘要（原文）

> Neural radiance field (NeRF) is a promising approach for reconstruction and new view synthesis. However, previous NeRF-based reconstruction methods overlook the critical role of acoustic impedance in ultrasound imaging. Localization methods face challenges related to local minima due to the selection of initial poses. In this study, we design a robotic ultrasound system (RUSS) with an acoustic-impedance-aware ultrasound NeRF (AIA-UltraNeRF) to decouple the scanning and diagnostic processes. Specifically, AIA-UltraNeRF models a continuous function of hash-encoded spatial coordinates for the 3D ultrasound map, allowing for the storage of acoustic impedance without dense sampling. This approach accelerates both reconstruction and inference speeds. We then propose a dual-supervised network that leverages teacher and student models to hash-encode the rendered ultrasound images from the reconstructed map. AIA-UltraNeRF retrieves the most similar hash values without the need to render images again, providing an offline initial image position for localization. Moreover, we develop a RUSS with a spherical remote center of motion mechanism to hold the probe, implementing operator-independent scanning modes that separate image acquisition from diagnostic workflows. Experimental results on a phantom and human subjects demonstrate the effectiveness of acoustic impedance in implicitly characterizing the color of ultrasound images. AIAUltraNeRF achieves both reconstruction and localization with inference speeds that are 9.9 faster than those of vanilla NeRF.

