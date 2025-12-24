---
layout: default
title: "SoK: Cybersecurity Assessment of Humanoid Ecosystem"
---

# SoK: Cybersecurity Assessment of Humanoid Ecosystem

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17481" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17481v2</a>
  <a href="https://arxiv.org/pdf/2508.17481.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17481v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17481v2', 'SoK: Cybersecurity Assessment of Humanoid Ecosystem')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Priyanka Prakash Surve, Asaf Shabtai, Yuval Elovici

**分类**: cs.CR, cs.RO

**发布日期**: 2025-08-24 (更新: 2025-09-01)

---

## 💡 一句话要点

**提出七层安全模型以评估类人机器人生态系统的网络安全**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `网络安全` `类人机器人` `系统化知识` `攻击防御模型` `安全评估` `蒙特卡洛分析` `风险管理`

## 📋 核心要点

1. 现有研究主要集中于特定威胁，未能全面考虑攻击对机器人互联系统的影响。
2. 提出一个七层安全模型，整合39种攻击和35种防御措施，提供系统化的安全评估方法。
3. 通过对三款实际机器人的评估，发现其安全成熟度得分在39.9%到79.5%之间，显示出显著的安全差异。

## 📝 摘要（中文）

类人机器人在医疗、工业、国防和服务等领域的实际部署正在不断推进。尽管通常被视为网络物理系统（CPS），但其对传统网络软件栈的依赖使其面临独特的安全风险。现有研究主要集中在特定威胁上，如LiDAR欺骗或对抗性机器学习，未能全面考虑攻击如何影响机器人互联系统。本文通过系统化知识（SoK）的方法，提出了一个七层安全模型，整合了39种已知攻击和35种防御措施，涵盖从硬件到人机交互的整个生态系统。基于该模型，构建了一个量化的39x35攻击-防御矩阵，并通过蒙特卡洛分析进行了验证，评估了三款实际机器人，显示出不同的安全成熟度水平。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在网络安全评估方面的不足，现有方法未能全面考虑攻击对整个系统的影响。

**核心思路**：通过系统化知识的方法，提出一个七层安全模型，整合不同领域的研究成果，以全面评估类人机器人的安全性。

**技术框架**：整体架构包括七层安全模型，涵盖硬件、软件、通信和人机交互等方面，并构建39x35的攻击-防御矩阵。

**关键创新**：提出的七层安全模型和量化的攻击-防御矩阵是本文的核心创新，与现有方法相比，提供了更全面的安全评估视角。

**关键设计**：在攻击-防御矩阵中，采用风险加权评分，并通过蒙特卡洛分析验证模型的有效性，确保评估结果的可靠性。

## 📊 实验亮点

实验结果显示，三款机器人在安全成熟度方面存在显著差异，得分范围为39.9%到79.5%。这一量化评估方法为跨平台的安全基准测试提供了依据，支持安全投资的优先级排序。

## 🎯 应用场景

该研究为类人机器人在医疗、工业和服务等领域的安全评估提供了系统化的方法，能够帮助开发者识别和优先处理安全风险，提升机器人系统的整体安全性。未来，该模型可扩展至其他类型的机器人和网络物理系统，推动相关领域的安全研究与实践。

## 📄 摘要（原文）

> Humanoids are progressing toward practical deployment across healthcare, industrial, defense, and service sectors. While typically considered cyber-physical systems (CPSs), their dependence on traditional networked software stacks (e.g., Linux operating systems), robot operating system (ROS) middleware, and over-the-air update channels, creates a distinct security profile that exposes them to vulnerabilities conventional CPS models do not fully address. Prior studies have mainly examined specific threats, such as LiDAR spoofing or adversarial machine learning (AML). This narrow focus overlooks how an attack targeting one component can cascade harm throughout the robot's interconnected systems. We address this gap through a systematization of knowledge (SoK) that takes a comprehensive approach, consolidating fragmented research from robotics, CPS, and network security domains. We introduce a seven-layer security model for humanoid robots, organizing 39 known attacks and 35 defenses across the humanoid ecosystem-from hardware to human-robot interaction. Building on this security model, we develop a quantitative 39x35 attack-defense matrix with risk-weighted scoring, validated through Monte Carlo analysis. We demonstrate our method by evaluating three real-world robots: Pepper, G1 EDU, and Digit. The scoring analysis revealed varying security maturity levels, with scores ranging from 39.9% to 79.5% across the platforms. This work introduces a structured, evidence-based assessment method that enables systematic security evaluation, supports cross-platform benchmarking, and guides prioritization of security investments in humanoid robotics.

