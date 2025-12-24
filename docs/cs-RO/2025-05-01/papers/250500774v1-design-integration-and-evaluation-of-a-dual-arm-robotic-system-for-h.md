---
layout: default
title: Design, Integration, and Evaluation of a Dual-Arm Robotic System for High Throughput Tissue Sampling from Potato Tubers
---

# Design, Integration, and Evaluation of a Dual-Arm Robotic System for High Throughput Tissue Sampling from Potato Tubers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00774" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00774v1</a>
  <a href="https://arxiv.org/pdf/2505.00774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00774v1', 'Design, Integration, and Evaluation of a Dual-Arm Robotic System for High Throughput Tissue Sampling from Potato Tubers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divyanth L. G., Syed Usama Bin Sabir, Divya Rathore, Lav R. Khot, Chakradhar Mattupalli, Manoj Karkee

**分类**: cs.RO

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出双臂机器人系统以解决马铃薯块茎组织采样问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `双臂机器人` `组织采样` `机器视觉` `农业自动化` `高通量检测`

## 📋 核心要点

1. 现有手动组织提取方法劳动强度高，效率低，难以满足现代农业需求。
2. 本研究提出了一种双臂机器人系统，结合机器视觉技术，实现自动化的块茎组织采样。
3. 实验结果表明，该系统在采样精度和效率上显著优于传统手动方法，成功率达到81.5%。

## 📝 摘要（中文）

手动从马铃薯块茎提取组织以进行分子病原体检测非常繁琐。本研究提出了一种机器视觉引导的双臂协调在线机器人系统，集成了块茎抓取和组织采样机制。块茎通过输送带运输，当YOLOv11视觉系统检测到块茎时，单自由度机械臂会停止并抓取块茎进行定位。第二个机械臂则使用基于YOLOv10的视觉系统识别采样位置，执行组织提取。系统在块茎表面位置误差为1.84mm，深度偏差为1.79mm，核心提取和沉积成功率为81.5%，平均采样周期为10.4秒，总成本低于1900美元，展示了其作为成本效益替代方案的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决手动从马铃薯块茎提取组织的高劳动强度和低效率问题。现有方法不仅耗时长，而且对操作人员的技能要求高，难以实现高通量采样。

**核心思路**：论文提出了一种机器视觉引导的双臂机器人系统，通过自动化抓取和采样过程，减少人工干预，提高采样效率和准确性。系统设计旨在实现高通量的组织提取，适应现代农业的需求。

**技术框架**：系统整体架构包括两个主要模块：第一是基于YOLOv11的视觉系统，用于检测块茎并控制单自由度机械臂抓取；第二是基于YOLOv10的视觉系统，指导三自由度笛卡尔机械臂进行组织采样。采样过程分为四个阶段：插入、旋转、回撤和沉积。

**关键创新**：最重要的技术创新在于将机器视觉与双臂协调控制相结合，实现了块茎的自动化抓取和高效采样。这种设计显著提高了采样的成功率和速度，区别于传统的手动方法。

**关键设计**：系统采用了YOLOv11和YOLOv10作为视觉识别模块，确保了块茎和采样位置的准确检测。机械臂的抓取和采样动作经过精确编程，确保了在块茎表面和深度上的高精度操作。

## 📊 实验亮点

实验结果显示，该系统在块茎表面位置误差为1.84mm，深度偏差为1.79mm，核心提取和沉积成功率达到81.5%。平均采样周期为10.4秒，显示出其在效率和准确性上的显著提升。系统组件总成本低于1900美元，具备良好的经济性。

## 🎯 应用场景

该研究的双臂机器人系统具有广泛的应用潜力，特别是在农业领域的病原体检测和植物健康监测中。通过实现高通量的组织采样，该系统能够显著提高农业生产效率，降低人工成本，推动农业自动化发展。未来，该系统还可扩展到其他作物的组织提取和分析中。

## 📄 摘要（原文）

> Manual tissue extraction from potato tubers for molecular pathogen detection is highly laborious. This study presents a machine-vision-guided, dual-arm coordinated inline robotic system integrating tuber grasping and tissue sampling mechanisms. Tubers are transported on a conveyor that halts when a YOLOv11-based vision system detects a tuber within the workspace of a one-prismatic-degree-of-freedom (P-DoF) robotic arm. This arm, equipped with a gripping end-effector, secures and positions the tuber for sampling. The second arm, a 3-P-DoF Cartesian manipulator with a biopsy punch-based end-effector, then performs tissue extraction guided by a YOLOv10-based vision system that identifies the sampling sites on the tuber such as eyes or stolon scars. The sampling involves four stages: insertion of the punch into the tuber, punch rotation for tissue detachment, biopsy punch retraction, and deposition of the tissue core onto a collection site. The system achieved an average positional error of 1.84 mm along the tuber surface and a depth deviation of 1.79 mm from a 7.00 mm target. The success rate for core extraction and deposition was 81.5%, with an average sampling cycle of 10.4 seconds. The total cost of the system components was under $1,900, demonstrating the system's potential as a cost-effective alternative to labor-intensive manual tissue sampling. Future work will focus on optimizing for multi-site sampling from a single tuber and validation in commercial settings.

