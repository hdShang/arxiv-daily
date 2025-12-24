---
layout: default
title: "MILE: A Mechanically Isomorphic Exoskeleton Data Collection System with Fingertip Visuotactile Sensing for Dexterous Manipulation"
---

# MILE: A Mechanically Isomorphic Exoskeleton Data Collection System with Fingertip Visuotactile Sensing for Dexterous Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00324" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00324v1</a>
  <a href="https://arxiv.org/pdf/2512.00324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.00324v1', 'MILE: A Mechanically Isomorphic Exoskeleton Data Collection System with Fingertip Visuotactile Sensing for Dexterous Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinda Du, Jieji Ren, Qiaojun Yu, Ningbin Zhang, Yu Deng, Xingyu Wei, Yufei Liu, Guoying Gu, Xiangyang Zhu

**分类**: cs.RO, cs.CV, cs.HC

**发布日期**: 2025-11-29

---

## 💡 一句话要点

**MILE：一种机械同构外骨骼数据采集系统，配备指尖视觉触觉传感，用于灵巧操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `灵巧操作` `模仿学习` `遥操作` `机械同构` `视觉触觉` `数据采集` `外骨骼` `机器人手`

## 📋 核心要点

1. 现有灵巧操作模仿学习方法受限于缺乏大规模、高保真度的数据集，数据采集流程存在运动重定向不准确等问题。
2. MILE系统通过机械同构设计，从人手到外骨骼再到机械手，消除了非线性重定向，实现了精确控制。
3. 实验表明，MILE系统遥操作成功率提升64%，结合指尖触觉观测比仅视觉基线成功率提升25%，验证了数据集的有效性。

## 📝 摘要（中文）

模仿学习在灵巧手部操作方面展现出潜力，但其有效性受限于缺乏大规模、高保真度的数据。现有的数据采集流程存在运动重定向不准确、数据采集效率低以及缺少高分辨率指尖触觉感知等问题。为了解决这些问题，我们提出了MILE，一个机械同构的遥操作和数据采集系统，该系统从人手到外骨骼再到机械手进行了协同设计。外骨骼在人体测量学上源于人手，而机械手保留了一对一的关节位置同构，消除了非线性重定向，实现了精确、自然的控制。外骨骼实现了低于一度的多关节平均绝对角度误差，而机械手集成了紧凑的指尖视觉触觉模块，提供了高分辨率的触觉观测。基于这种无需重定向的界面，我们遥操作复杂的、接触丰富的掌内操作，并高效地收集包含高分辨率指尖视觉触觉信号、RGB-D图像和关节位置的多模态数据集。遥操作流程的平均成功率提高了64%。与仅使用视觉的基线相比，结合指尖触觉观测进一步将成功率平均提高了25%，验证了数据集的保真度和效用。

## 🔬 方法详解

**问题定义**：论文旨在解决灵巧手部操作模仿学习中，缺乏高质量数据集的问题。现有数据采集方法存在运动重定向误差大、采集效率低、缺乏高分辨率触觉信息等痛点，限制了模仿学习算法的性能。

**核心思路**：论文的核心思路是设计一个机械同构的遥操作系统，保证人手、外骨骼和机械手之间关节位置的一一对应关系，从而避免复杂的非线性运动重定向。同时，在机械手指尖集成高分辨率的视觉触觉传感器，获取丰富的触觉信息。

**技术框架**：MILE系统包含三个主要部分：人手佩戴的外骨骼、机械手以及连接两者的遥操作控制系统。外骨骼负责捕捉人手的运动，机械手负责执行操作任务。遥操作控制系统将外骨骼的运动指令传递给机械手，并接收机械手的视觉和触觉反馈。整个系统避免了复杂的运动学逆解和重定向过程。

**关键创新**：MILE系统的关键创新在于其机械同构的设计理念，以及指尖视觉触觉传感器的集成。机械同构保证了运动控制的精确性，而指尖视觉触觉传感器提供了丰富的触觉信息，有助于提高操作的鲁棒性和精度。

**关键设计**：外骨骼的设计基于人体测量学数据，保证了佩戴的舒适性和运动的自然性。机械手的关节设计与人手一一对应，保证了运动的同构性。指尖视觉触觉传感器采用紧凑型设计，不影响机械手的灵活性。遥操作控制系统采用低延迟的通信协议，保证了操作的实时性。

## 📊 实验亮点

实验结果表明，MILE系统能够显著提高遥操作的成功率。与传统方法相比，MILE系统的遥操作流程的平均成功率提高了64%。此外，结合指尖触觉观测进一步将成功率平均提高了25%（与仅使用视觉的基线相比）。这些结果验证了MILE系统的数据采集能力和触觉信息的有效性。

## 🎯 应用场景

该研究成果可应用于远程操作、康复训练、虚拟现实等领域。例如，在危险环境中，操作人员可以通过MILE系统远程控制机械手进行精细操作。在康复训练中，可以利用该系统辅助患者进行手部功能恢复。在虚拟现实中，可以提供更真实的触觉反馈，增强用户的沉浸感。

## 📄 摘要（原文）

> Imitation learning provides a promising approach to dexterous hand manipulation, but its effectiveness is limited by the lack of large-scale, high-fidelity data. Existing data-collection pipelines suffer from inaccurate motion retargeting, low data-collection efficiency, and missing high-resolution fingertip tactile sensing. We address this gap with MILE, a mechanically isomorphic teleoperation and data-collection system co-designed from human hand to exoskeleton to robotic hand. The exoskeleton is anthropometrically derived from the human hand, and the robotic hand preserves one-to-one joint-position isomorphism, eliminating nonlinear retargeting and enabling precise, natural control. The exoskeleton achieves a multi-joint mean absolute angular error below one degree, while the robotic hand integrates compact fingertip visuotactile modules that provide high-resolution tactile observations. Built on this retargeting-free interface, we teleoperate complex, contact-rich in-hand manipulation and efficiently collect a multimodal dataset comprising high-resolution fingertip visuotactile signals, RGB-D images, and joint positions. The teleoperation pipeline achieves a mean success rate improvement of 64%. Incorporating fingertip tactile observations further increases the success rate by an average of 25% over the vision-only baseline, validating the fidelity and utility of the dataset. Further details are available at: https://sites.google.com/view/mile-system.

