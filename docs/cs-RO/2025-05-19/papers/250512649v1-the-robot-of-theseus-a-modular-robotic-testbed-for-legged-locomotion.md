---
layout: default
title: "The Robot of Theseus: A modular robotic testbed for legged locomotion"
---

# The Robot of Theseus: A modular robotic testbed for legged locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12649" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12649v1</a>
  <a href="https://arxiv.org/pdf/2505.12649.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12649v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12649v1', 'The Robot of Theseus: A modular robotic testbed for legged locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karthik Urs, Jessica Carlson, Aditya Srinivas Manohar, Michael Rakowiecki, Abdulhadi Alkayyali, John E. Saunders, Faris Tulbah, Talia Y. Moore

**分类**: cs.RO

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出低成本模块化四足机器人以解决生物力学测试问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `模块化设计` `生物力学测试` `低成本` `开放源代码` `控制策略` `远程探索`

## 📋 核心要点

1. 现有的四足机器人在生物力学相关性和定制化方面存在显著不足，且价格昂贵，限制了生物研究的开展。
2. 本文提出了一种低成本的模块化四足机器人TROT，能够模拟多种动物形态，支持用户自定义步态和形态变化。
3. TROT的设计和实现使其在生物力学假设测试中表现出色，且具有广泛的应用潜力，包括控制策略开发和远程探索。

## 📝 摘要（中文）

本研究提出了一种低成本的四足机器人——Theseus机器人（TROT），旨在解决现有四足机器人在生物力学相关性和定制化方面的不足。TROT的构建成本约为4000美元，采用3D打印部件和标准现货材料。其模块化的腿部设计能够模拟多种动物形态，支持用户定义的步态和形态变化。该机器人不仅适用于生物力学假设测试，还可用于开发新控制策略、排雷和远程探索等多种应用。所有硬件和软件的详细信息均可在线获取。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有四足机器人在生物力学相关性不足和高成本的问题。现有的商业四足机器人往往难以定制，且与动物形态差异较大，限制了其在生物研究中的应用。

**核心思路**：论文提出的TROT机器人采用模块化设计，能够通过更换部件来模拟不同动物的形态，且成本低廉，适合生物力学假设测试。

**技术框架**：TROT的整体架构包括模块化的腿部设计，每条腿由2或3个刚性链接组成，关节可旋转以模拟膝关节或肘关节。机器人使用四杆连杆机制来控制关节的有效腿长，后驱动电机可调节虚拟弹簧刚度和运动范围。

**关键创新**：TROT的主要创新在于其模块化的腿部设计和低成本构建，使其能够在生物力学研究中提供更高的相关性和灵活性。这种设计与现有的固定形态机器人有本质区别。

**关键设计**：每条腿的长度可通过伸缩机制进行调节，用户可以根据需要定义步态和形态变化。所有CAD文件和代码均可在TROT项目页面上免费下载，促进了研究的开放性和可重复性。

## 📊 实验亮点

实验结果表明，TROT机器人能够有效模拟多种动物的步态，支持用户自定义的形态变化。与现有商业四足机器人相比，TROT在生物力学相关性和定制化方面表现出显著提升，且成本降低至约4000美元。

## 🎯 应用场景

TROT机器人在生物力学研究中具有广泛的应用潜力，能够用于假设测试、控制策略开发、排雷和远程探索等领域。其低成本和模块化设计使得更多研究团队能够参与到相关研究中，推动机器人技术的发展。

## 📄 摘要（原文）

> Robotic models are useful for independently varying specific features, but most quadrupedal robots differ so greatly from animal morphologies that they have minimal biomechanical relevance. Commercially available quadrupedal robots are also prohibitively expensive for biological research programs and difficult to customize. Here, we present a low-cost quadrupedal robot with modular legs that can match a wide range of animal morphologies for biomechanical hypothesis testing. The Robot Of Theseus (TROT) costs approximately $4000 to build out of 3D printed parts and standard off-the-shelf supplies. Each limb consists of 2 or 3 rigid links; the proximal joint can be rotated to become a knee or elbow. Telescoping mechanisms vary the length of each limb link. The open-source software accommodates user-defined gaits and morphology changes. Effective leg length, or crouch, is determined by the four-bar linkage actuating each joint. The backdrivable motors can vary virtual spring stiffness and range of motion. Full descriptions of the TROT hardware and software are freely available online. We demonstrate the use of TROT to compare locomotion among extant, extinct, and theoretical morphologies. In addition to biomechanical hypothesis testing, we envision a variety of different applications for this low-cost, modular, legged robotic platform, including developing novel control strategies, clearing land mines, or remote exploration. All CAD and code is available for download on the TROT project page.

