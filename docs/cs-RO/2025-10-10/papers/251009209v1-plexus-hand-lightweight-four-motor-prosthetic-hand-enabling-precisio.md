---
layout: default
title: PLEXUS Hand: Lightweight Four-Motor Prosthetic Hand Enabling Precision-Lateral Dexterous Manipulation
---

# PLEXUS Hand: Lightweight Four-Motor Prosthetic Hand Enabling Precision-Lateral Dexterous Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09209" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09209v1</a>
  <a href="https://arxiv.org/pdf/2510.09209.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09209v1" onclick="toggleFavorite(this, '2510.09209v1', 'PLEXUS Hand: Lightweight Four-Motor Prosthetic Hand Enabling Precision-Lateral Dexterous Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuki Kuroda, Tomoya Takahashi, Cristian C Beltran-Hernandez, Masashi Hamaya, Kazutoshi Tanaka

**分类**: cs.RO

**发布日期**: 2025-10-10

**期刊**: 2025 International Conference On Rehabilitation Robotics (ICORR), Chicago, IL, USA, 2025, pp. 22-29

**DOI**: [10.1109/ICORR66766.2025.11063043](https://doi.org/10.1109/ICORR66766.2025.11063043)

---

## 💡 一句话要点

**PLEXUS Hand：轻量化四电机假肢手，实现精确横向灵巧操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `电动假肢手` `灵巧操作` `手内操作` `轻量化设计` `单轴拇指`

## 📋 核心要点

1. 现有电动假肢手笨重、电机易损，且缺乏手内灵巧操作能力，难以满足日常使用需求。
2. 该论文提出一种轻量化四电机假肢手，通过单轴拇指和优化拇指位置实现精确和横向抓握间的重定向。
3. 实验结果表明，该假肢手在物体重定向、设备插入和工具操作等任务中表现出较高的成功率。

## 📝 摘要（中文）

电动假肢手需要轻量化以减轻用户负担，外形需接近人手以满足美观需求，电机内置以避免损坏和污染。除了执行日常活动的能力外，这些特性对于假肢手的日常使用至关重要。手内操作对于执行日常活动是必要的，例如在不同姿势之间转换，特别是通过旋转运动，例如在插入卡片之前重新调整卡片方向以及操作螺丝刀等工具。然而，目前使用的电动假肢手仅能实现静态抓握姿势，而现有的操作方法要么需要大量电机，这使得假肢手对于日常使用来说过于笨重，要么需要复杂的机构，这需要很大的内部空间并迫使外部电机放置，从而使附件复杂化并将组件暴露于损坏。作为替代方案，我们结合了单轴拇指和优化的拇指位置，仅使用四个电机在一个轻量级（311克）的假肢手中实现了基本姿势和手内操作，即精确抓握和横向抓握之间的重新定向。使用各种宽度（5-30毫米）和形状（圆柱体和棱柱体）的原始对象进行的实验验证表明，重新定向任务的成功率达到90-100%。该假肢手可以执行盖章和USB设备插入，以及旋转操作螺丝刀。

## 🔬 方法详解

**问题定义**：现有电动假肢手通常存在重量大、内部空间受限、电机易损坏以及缺乏灵巧操作能力等问题。这些问题限制了假肢手的日常使用，尤其是在需要手内操作的场景下，例如调整物体方向或使用工具。现有方法要么需要大量电机，导致重量增加，要么需要复杂的机械结构，占用内部空间，并且电机外置容易损坏。

**核心思路**：该论文的核心思路是通过优化拇指的设计和位置，结合少量电机，实现轻量化和灵巧操作的平衡。具体来说，采用单轴拇指设计，并优化拇指的位置，使其能够支持精确抓握和横向抓握之间的转换，从而实现手内操作。

**技术框架**：该假肢手的整体架构包括四个电机，分别控制拇指的旋转、手指的屈伸以及手腕的运动（具体控制方式未知）。通过优化拇指的运动轨迹和与其他手指的协同，实现不同的抓握姿势和手内操作。该设计旨在最小化电机数量和重量，同时最大化操作的灵活性。

**关键创新**：该论文的关键创新在于通过单轴拇指和优化的拇指位置，仅使用四个电机就实现了基本的姿势和手内操作，即精确抓握和横向抓握之间的重新定向。这种设计在轻量化和灵巧操作之间取得了较好的平衡，克服了现有假肢手的局限性。

**关键设计**：拇指采用单轴旋转设计，具体旋转角度范围和控制策略未知。拇指的位置经过优化，能够与其他手指配合完成不同的抓握姿势。论文中提到假肢手的重量为311克，但未提供其他关键参数设置、损失函数或网络结构等技术细节。

## 📊 实验亮点

实验结果表明，该假肢手在各种宽度（5-30毫米）和形状（圆柱体和棱柱体）的物体重定向任务中，成功率达到90-100%。此外，该假肢手还成功执行了盖章、USB设备插入以及旋转操作螺丝刀等任务，验证了其在实际应用中的可行性。这些实验结果表明，该假肢手在灵巧操作方面具有显著的优势。

## 🎯 应用场景

该研究成果可应用于开发更轻便、更灵活的电动假肢手，提高残疾人士的日常生活质量。该假肢手能够执行物体重定向、设备插入和工具操作等任务，使其在家庭、工作场所和康复训练等场景中具有广泛的应用前景。未来，该技术有望进一步发展，实现更复杂的手内操作和更自然的人机交互。

## 📄 摘要（原文）

> Electric prosthetic hands should be lightweight to decrease the burden on the user, shaped like human hands for cosmetic purposes, and have motors inside to protect them from damage and dirt. In addition to the ability to perform daily activities, these features are essential for everyday use of the hand. In-hand manipulation is necessary to perform daily activities such as transitioning between different postures, particularly through rotational movements, such as reorienting cards before slot insertion and operating tools such as screwdrivers. However, currently used electric prosthetic hands only achieve static grasp postures, and existing manipulation approaches require either many motors, which makes the prosthesis heavy for daily use in the hand, or complex mechanisms that demand a large internal space and force external motor placement, complicating attachment and exposing the components to damage. Alternatively, we combine a single-axis thumb and optimized thumb positioning to achieve basic posture and in-hand manipulation, that is, the reorientation between precision and lateral grasps, using only four motors in a lightweight (311 g) prosthetic hand. Experimental validation using primitive objects of various widths (5-30 mm) and shapes (cylinders and prisms) resulted in success rates of 90-100% for reorientation tasks. The hand performed seal stamping and USB device insertion, as well as rotation to operate a screwdriver.

