---
layout: default
title: Safe Payload Transfer with Ship-Mounted Cranes: A Robust Model Predictive Control Approach
---

# Safe Payload Transfer with Ship-Mounted Cranes: A Robust Model Predictive Control Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16953" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16953v1</a>
  <a href="https://arxiv.org/pdf/2510.16953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16953v1" onclick="toggleFavorite(this, '2510.16953v1', 'Safe Payload Transfer with Ship-Mounted Cranes: A Robust Model Predictive Control Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ersin Das, William A. Welch, Patrick Spieler, Keenan Albee, Aurelio Noca, Jeffrey Edlund, Jonathan Becktor, Thomas Touma, Jessica Todd, Sriramya Bhamidipati, Stella Kombo, Maira Saboia, Anna Sabel, Grace Lim, Rohan Thakker, Amir Rahmani, Joel W. Burdick

**分类**: eess.SY, cs.RO

**发布日期**: 2025-10-19

---

## 💡 一句话要点

**提出基于鲁棒MPC的船载起重机安全有效载荷转移方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `船载起重机` `模型预测控制` `鲁棒控制` `控制障碍函数` `安全控制`

## 📋 核心要点

1. 船载起重机在恶劣海况下作业，易受外部扰动影响，传统控制方法难以保证载荷转移的安全性和精度。
2. 提出基于鲁棒MPC的控制框架，结合R-ZOCBF安全约束和时变边界框避障，确保载荷安全。
3. 引入在线鲁棒性参数自适应方案，降低R-ZOCBF的保守性，并在5自由度起重机原型上验证了方法的有效性。

## 📝 摘要（中文）

本文提出了一种鲁棒且安全的模型预测控制（MPC）框架，用于解决非结构化运输环境中船载起重机的安全实时控制问题。与传统起重机系统不同，船载起重机持续受到显著的外部扰动，这些扰动源于船舶在恶劣海况下的动态运动响应，影响了欠驱动起重机的动力学，可能导致鲁棒性问题。该方法在一个5自由度起重机系统上进行了验证，该系统使用Stewart平台模拟海洋表面运动对支撑船只的外部扰动。起重机有效载荷转移操作必须避开障碍物，并将有效载荷精确放置在指定的目标区域内。在非线性MPC中，使用基于鲁棒零阶控制障碍函数（R-ZOCBF）的安全约束来确保有效载荷的安全定位，同时使用时变边界框进行避碰。引入了一种新的基于优化的在线鲁棒性参数自适应方案，以减少R-ZOCBF的保守性。起重机原型上的实验表明，该安全控制方法在起重机底座受到显著扰动运动下的整体性能良好。虽然重点是起重机辅助转移，但该方法更普遍地适用于安全机器人辅助的零件配合和零件插入。

## 🔬 方法详解

**问题定义**：论文旨在解决船载起重机在复杂海洋环境下安全可靠地转移有效载荷的问题。现有方法难以同时处理船舶运动带来的外部扰动、避障需求以及目标位置的精确到达，尤其是在保证安全性的前提下，传统的控制方法往往过于保守。

**核心思路**：论文的核心思路是利用鲁棒模型预测控制（MPC）框架，结合鲁棒零阶控制障碍函数（R-ZOCBF）来保证安全性，并采用在线鲁棒性参数自适应方案来降低R-ZOCBF的保守性。通过预测未来状态并优化控制输入，同时考虑安全约束和性能指标，实现安全高效的载荷转移。

**技术框架**：整体框架包括以下几个主要模块：1) 状态估计：通过传感器获取起重机和船舶的状态信息。2) 模型预测：利用起重机动力学模型预测未来一段时间内的状态。3) 安全约束：使用R-ZOCBF定义安全区域，防止碰撞和超出工作范围。4) 避障：采用时变边界框来描述障碍物，并将其纳入优化问题中。5) 优化求解：通过求解非线性优化问题，得到最优的控制输入。6) 控制执行：将控制输入作用于起重机，实现载荷转移。

**关键创新**：论文的关键创新在于：1) 将R-ZOCBF应用于船载起重机的安全控制，保证了在存在扰动情况下的安全性。2) 提出了在线鲁棒性参数自适应方案，能够根据实际情况调整R-ZOCBF的保守程度，提高了控制性能。3) 将时变边界框用于动态避障，使得起重机能够在复杂环境中安全作业。

**关键设计**：R-ZOCBF的设计需要选择合适的障碍函数，并确定鲁棒性参数。在线鲁棒性参数自适应方案通过优化一个目标函数来调整鲁棒性参数，该目标函数旨在最小化R-ZOCBF的保守程度，同时保证安全性。时变边界框的生成需要根据障碍物的运动轨迹进行预测，并选择合适的边界框大小。

## 📊 实验亮点

实验结果表明，所提出的鲁棒MPC方法能够在显著的船舶运动扰动下，安全地将有效载荷转移到目标区域。通过在线鲁棒性参数自适应，R-ZOCBF的保守性得到了有效降低，控制性能得到了提升。实验验证了该方法在实际船载起重机系统中的可行性和有效性，为复杂环境下的机器人安全控制提供了新的解决方案。

## 🎯 应用场景

该研究成果可应用于多种需要安全可靠的机器人操作场景，例如：海上石油平台的设备维护、港口码头的货物装卸、以及其他需要在复杂环境中进行精确操作的领域。该方法能够提高作业效率，降低安全风险，并为自动化操作提供技术支持，具有重要的实际应用价值和广阔的应用前景。

## 📄 摘要（原文）

> Ensuring safe real-time control of ship-mounted cranes in unstructured transportation environments requires handling multiple safety constraints while maintaining effective payload transfer performance. Unlike traditional crane systems, ship-mounted cranes are consistently subjected to significant external disturbances affecting underactuated crane dynamics due to the ship's dynamic motion response to harsh sea conditions, which can lead to robustness issues. To tackle these challenges, we propose a robust and safe model predictive control (MPC) framework and demonstrate it on a 5-DOF crane system, where a Stewart platform simulates the external disturbances that ocean surface motions would have on the supporting ship. The crane payload transfer operation must avoid obstacles and accurately place the payload within a designated target area. We use a robust zero-order control barrier function (R-ZOCBF)-based safety constraint in the nonlinear MPC to ensure safe payload positioning, while time-varying bounding boxes are utilized for collision avoidance. We introduce a new optimization-based online robustness parameter adaptation scheme to reduce the conservativeness of R-ZOCBFs. Experimental trials on a crane prototype demonstrate the overall performance of our safe control approach under significant perturbing motions of the crane base. While our focus is on crane-facilitated transfer, the methods more generally apply to safe robotically-assisted parts mating and parts insertion.

