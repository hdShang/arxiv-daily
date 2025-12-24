---
layout: default
title: "Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents"
---

# Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23450" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23450v2</a>
  <a href="https://arxiv.org/pdf/2505.23450.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23450v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23450v2', 'Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, Lichao Sun

**分类**: cs.RO

**发布日期**: 2025-05-29 (更新: 2025-06-11)

**备注**: 20 pages, 8 figures

---

## 💡 一句话要点

**提出Agentic Robot框架以解决长时间机器人操作中的错误累积问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间操作` `机器人技术` `视觉-语言-行动` `标准化行动程序` `自我验证` `智能系统` `错误恢复`

## 📋 核心要点

1. 现有的机器人操作方法在长时间任务中容易出现错误累积，缺乏有效的执行验证机制，影响了系统的可靠性。
2. 本文提出的Agentic Robot框架通过标准化行动程序（SAP）实现了组件间的协调，增强了操作的可靠性和可解释性。
3. 在LIBERO基准测试中，Agentic Robot的平均成功率达到79.6%，超越了其他基线方法，显示出显著的性能提升。

## 📝 摘要（中文）

长时间的机器人操作面临显著挑战，要求系统具备扩展推理、精确执行和强大的错误恢复能力。现有方法，无论是基于静态规划还是端到端的视觉运动策略，都存在错误累积和缺乏有效验证机制的问题，限制了其在现实场景中的可靠性。本文提出了Agentic Robot，一个受脑启发的框架，通过标准化行动程序（SAP）解决这些局限。SAP建立了结构化的工作流程，涵盖规划、执行和验证阶段。该架构包括三个专门组件：大型推理模型、视觉-语言-行动执行器和时间验证器。实验结果表明，Agentic Robot在LIBERO基准测试中实现了79.6%的平均成功率，超越了SpatialVLA和OpenVLA，展示了其在顺序操作中的性能和可解释性提升。

## 🔬 方法详解

**问题定义**：本文旨在解决长时间机器人操作中的错误累积和缺乏有效验证的问题。现有方法在复杂任务中表现不佳，导致执行不可靠。

**核心思路**：Agentic Robot框架通过引入标准化行动程序（SAP），模仿人类组织中的标准操作程序，建立结构化的工作流程，从而提升任务的执行和验证能力。

**技术框架**：该框架包括三个主要组件：1) 大型推理模型，负责将高层指令分解为语义一致的子目标；2) 视觉-语言-行动执行器，实时生成控制指令；3) 时间验证器，通过自我评估实现自主进展和错误恢复。

**关键创新**：SAP驱动的闭环设计支持动态自我验证，无需外部监督，这是与现有方法的本质区别，显著提升了系统的可靠性。

**关键设计**：框架中的关键设计包括推理模型的结构、执行器的控制命令生成机制，以及验证器的自我评估策略，这些设计共同支持了系统的高效运行。

## 📊 实验亮点

在LIBERO基准测试中，Agentic Robot实现了79.6%的平均成功率，超越了SpatialVLA和OpenVLA，分别提升了6.1%和7.4%。这些结果表明，SAP驱动的协调机制显著增强了顺序操作的性能和可解释性。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能制造和服务机器人等，能够在复杂环境中进行长时间的操作任务。通过提升机器人在动态环境中的可靠性，未来可能推动更广泛的自动化应用，改善人机协作效率。

## 📄 摘要（原文）

> Long-horizon robotic manipulation poses significant challenges for autonomous systems, requiring extended reasoning, precise execution, and robust error recovery across complex sequential tasks. Current approaches, whether based on static planning or end-to-end visuomotor policies, suffer from error accumulation and lack effective verification mechanisms during execution, limiting their reliability in real-world scenarios. We present Agentic Robot, a brain-inspired framework that addresses these limitations through Standardized Action Procedure (SAP)--a novel coordination protocol governing component interactions throughout manipulation tasks. Drawing inspiration from Standardized Operating Procedures (SOPs) in human organizations, SAP establishes structured workflows for planning, execution, and verification phases. Our architecture comprises three specialized components: (1) a large reasoning model that decomposes high-level instructions into semantically coherent subgoals, (2) a vision-language-action executor that generates continuous control commands from real-time visual inputs, and (3) a temporal verifier that enables autonomous progression and error recovery through introspective assessment. This SAP-driven closed-loop design supports dynamic self-verification without external supervision. On the LIBERO benchmark, Agentic Robot achieves state-of-the-art performance with an average success rate of 79.6%, outperforming SpatialVLA by 6.1% and OpenVLA by 7.4% on long-horizon tasks. These results demonstrate that SAP-driven coordination between specialized components enhances both performance and interpretability in sequential manipulation, suggesting significant potential for reliable autonomous systems. Project Github: https://agentic-robot.github.io.

