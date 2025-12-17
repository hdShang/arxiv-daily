---
layout: default
title: Semi-Peaucellier Linkage and Differential Mechanism for Linear Pinching and Self-Adaptive Grasping
---

# Semi-Peaucellier Linkage and Differential Mechanism for Linear Pinching and Self-Adaptive Grasping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16524" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16524v1</a>
  <a href="https://arxiv.org/pdf/2510.16524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16524v1" onclick="toggleFavorite(this, '2510.16524v1', 'Semi-Peaucellier Linkage and Differential Mechanism for Linear Pinching and Self-Adaptive Grasping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haokai Ding, Zhaohan Chen, Tao Yang, Wenzeng Zhang

**分类**: cs.RO

**发布日期**: 2025-10-18

**备注**: 6 pages, 9 figures, Accepted author manuscript for IEEE CASE 2025

**期刊**: 2025 IEEE 21st International Conference on Automation Science and Engineering (CASE), Los Angeles, CA, USA, 2025, pp. 3441-3446

**DOI**: [10.1109/CASE58245.2025.11163785](https://doi.org/10.1109/CASE58245.2025.11163785)

---

## 💡 一句话要点

**提出SP-Diff平行夹爪系统，通过半反演连杆和差动机构实现线性夹取和自适应抓取。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人夹爪` `半反演连杆` `差动机构` `自适应抓取` `线性平行抓取` `行星齿轮传动` `工业自动化`

## 📋 核心要点

1. 传统末端执行器在智能工业自动化中适应性有限，难以应对多样化的工件和复杂的操作需求。
2. SP-Diff系统采用半反演连杆和差动机构，实现线性平行抓取和手指姿态的独立调整，提升了抓取的灵活性。
3. 实验表明，该系统能够自适应抓取各种工业工件和可变形物体，并降低了Z轴重新校准的需求。

## 📝 摘要（中文）

本文提出了一种SP-Diff平行夹爪系统，旨在解决智能工业自动化中传统末端执行器适应性有限的问题。该设计采用创新的差动连杆机构，具有模块化的对称双指配置，以实现线性平行抓取。通过集成行星齿轮传动，该系统能够在保持结构刚性的同时实现同步线性运动和独立的手指姿态调整，与弧形轨迹夹爪相比，Z轴重新校准需求降低了30%。紧凑的掌部结构包含经过运动学优化的平行四边形连杆机构和差动机构，展示了对各种工业工件和可变形物体（如柑橘类水果）的自适应抓取能力。嵌入了面向未来的接口，可用于潜在的力/视觉传感器集成，以促进数字孪生框架中的多模态数据采集（例如，轨迹规划和物体变形）。SP-Diff被设计为一种灵活的制造解决方案，通过其自适应架构提升了机器人末端执行器的智能，在协作机器人、物流自动化和专业操作场景中显示出有希望的应用。

## 🔬 方法详解

**问题定义**：传统工业夹爪在面对形状各异、材质不同的工件时，适应性较差。尤其是在需要精确线性夹取和姿态调整的场景下，现有夹爪往往需要复杂的控制和校准，效率较低。此外，对于易变形物体，传统夹爪容易造成损伤。

**核心思路**：SP-Diff系统的核心在于利用半反演连杆机构和差动机构，将旋转运动转化为线性运动，并实现手指姿态的独立控制。这种设计能够在保证结构刚性的前提下，提高夹爪的灵活性和适应性。通过行星齿轮传动，实现同步线性运动和独立手指姿态调整。

**技术框架**：SP-Diff系统采用模块化的对称双指配置。其主要组成部分包括：半反演连杆机构、差动机构、行星齿轮传动系统和紧凑的掌部结构。半反演连杆机构负责将旋转运动转化为线性运动，差动机构实现手指姿态的独立控制，行星齿轮传动系统保证同步线性运动，掌部结构则提供整体支撑和连接。

**关键创新**：该系统的关键创新在于将半反演连杆机构和差动机构相结合，实现了线性平行抓取和手指姿态的独立调整。这种设计突破了传统夹爪在灵活性和适应性方面的限制，能够更好地适应多样化的工件和复杂的操作需求。同时，紧凑的掌部结构设计也提高了系统的整体性能。

**关键设计**：行星齿轮传动系统的齿轮比是关键参数，它决定了线性运动和手指姿态调整之间的关系。平行四边形连杆机构的尺寸和角度也需要进行优化，以保证运动范围和精度。此外，力/视觉传感器的集成接口的设计也需要考虑数据采集和处理的需求。具体参数设置未知。

## 📊 实验亮点

SP-Diff系统通过集成行星齿轮传动，在保持结构刚性的同时实现了同步线性运动和独立的手指姿态调整，与弧形轨迹夹爪相比，Z轴重新校准需求降低了30%。该系统能够自适应抓取各种工业工件和可变形物体，例如柑橘类水果，展示了其在实际应用中的潜力。具体性能数据未知。

## 🎯 应用场景

SP-Diff系统在协作机器人、物流自动化和专业操作场景中具有广泛的应用前景。它可以用于抓取各种工业工件，包括形状不规则、易变形的物体。此外，该系统还可以应用于医疗器械、食品加工等领域，实现高精度、高可靠性的抓取操作。未来，通过集成力/视觉传感器，SP-Diff系统还可以实现更智能化的抓取和操作。

## 📄 摘要（原文）

> This paper presents the SP-Diff parallel gripper system, addressing the limited adaptability of conventional end-effectors in intelligent industrial automation. The proposed design employs an innovative differential linkage mechanism with a modular symmetric dual-finger configuration to achieve linear-parallel grasping. By integrating a planetary gear transmission, the system enables synchronized linear motion and independent finger pose adjustment while maintaining structural rigidity, reducing Z-axis recalibration requirements by 30% compared to arc-trajectory grippers. The compact palm architecture incorporates a kinematically optimized parallelogram linkage and Differential mechanism, demonstrating adaptive grasping capabilities for diverse industrial workpieces and deformable objects such as citrus fruits. Future-ready interfaces are embedded for potential force/vision sensor integration to facilitate multimodal data acquisition (e.g., trajectory planning and object deformation) in digital twin frameworks. Designed as a flexible manufacturing solution, SP-Diff advances robotic end-effector intelligence through its adaptive architecture, showing promising applications in collaborative robotics, logistics automation, and specialized operational scenarios.

