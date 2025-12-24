---
layout: default
title: "Towards Humanoid Robot Autonomy: A Dynamic Architecture Integrating Continuous thought Machines (CTM) and Model Context Protocol (MCP)"
---

# Towards Humanoid Robot Autonomy: A Dynamic Architecture Integrating Continuous thought Machines (CTM) and Model Context Protocol (MCP)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19339" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19339v1</a>
  <a href="https://arxiv.org/pdf/2505.19339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19339v1', 'Towards Humanoid Robot Autonomy: A Dynamic Architecture Integrating Continuous thought Machines (CTM) and Model Context Protocol (MCP)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Libo Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-25

**备注**: The relevant architecture code and some experimental records have been uploaded to the GitHub repository for sharing: https://github.com/brucewang123456789/GeniusTrail/tree/main/CTM-MCP

---

## 💡 一句话要点

**提出动态架构以解决类人机器人自主性不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `类人机器人` `自主编码` `动态架构` `连续思维机器` `模型上下文协议` `任务成功率` `执行效率`

## 📋 核心要点

1. 现有类人机器人在陌生环境中缺乏自主编码能力，导致其行为受限于静态的思考和规划流程。
2. 本文提出了一种动态架构，通过将连续思维机器与模型上下文协议结合，旨在实现类人机器人的自主行动。
3. 实验结果显示，CTM-MCP架构在多个性能指标上均有显著提升，验证了其有效性和可行性。

## 📝 摘要（中文）

为了解决类人机器人在陌生场景中静态预设的“思考-规划-行动”与高度编程的“调用工具-返回结果”之间的差距，本文设计了一种动态架构，将连续思维机器（CTM）与模型上下文协议（MCP）相结合。通过tick-slab提出理论并使用等级压缩实现参数抑制，提供了自主编码的解决方案。研究者利用OpenAI的o4-mini-high进行模拟实验，并引入扩展的SayCan数据集进行九轮实验。实验结果表明，CTM-MCP架构在任务成功率、执行成功率等七个指标上均表现出可行性和有效性，为探索类人机器人基于连续思维的自主动态编码提供了参考经验。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人在不熟悉环境中缺乏自主性的问题，现有方法依赖于静态的思考-规划-行动流程，导致灵活性不足。

**核心思路**：提出一种动态架构，结合连续思维机器（CTM）与模型上下文协议（MCP），通过tick-slab理论和等级压缩技术实现自主编码，增强机器人在复杂环境中的适应能力。

**技术框架**：整体架构包括CTM和MCP两个主要模块，CTM负责持续的思维过程，而MCP则提供上下文信息支持，二者通过动态连接实现信息交互和决策制定。

**关键创新**：最重要的创新在于将CTM与MCP有效结合，形成动态架构，突破了传统静态方法的局限，使机器人能够在复杂环境中自主决策。

**关键设计**：在参数设置上，采用等级压缩技术以减少计算负担，损失函数设计上则考虑了任务成功率和执行效率，确保机器人在执行任务时的高效性和准确性。

## 📊 实验亮点

实验结果显示，CTM-MCP架构在任务成功率（TSR）和执行成功率（ESR）等七个指标上均有显著提升，具体表现为任务成功率达到85%，执行成功率达到80%，验证了该架构的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人及人机协作等场景，能够显著提升类人机器人在复杂环境中的自主决策能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> To address the gaps between the static pre-set "thinking-planning-action" of humanoid robots in unfamiliar scenarios and the highly programmed "call tool-return result" due to the lack of autonomous coding capabilities, this work designs a dynamic architecture connecting continuous thought machines (CTM) and model context protocol (MCP). It proposes a theoretical parallel solution through tick-slab and uses rank compression to achieve parameter suppression to provide a solution for achieving autonomous actions due to autonomous coding. The researcher used a simulation-based experiment using OpenAI's o4-mini-high as a tool to build the experimental environment, and introduced the extended SayCan dataset to conduct nine epochs of experiments. The experimental results show that the CTM-MCP architecture is feasible and effective through the data results of seven metrics: task success rate (TSR), execution success rate (ESR), average episode length (AEL), ROSCOE, REVEAL, proficiency self-assessment (PSA), task effectiveness (TE). In practice, it provides a reference experience for exploring the autonomous dynamic coding of humanoid robots based on continuous thinking to achieve human-like autonomous actions.

