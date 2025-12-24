---
layout: default
title: "ASTREA: Introducing Agentic Intelligence for Orbital Thermal Autonomy"
---

# ASTREA: Introducing Agentic Intelligence for Orbital Thermal Autonomy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13380" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13380v2</a>
  <a href="https://arxiv.org/pdf/2509.13380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13380v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13380v2', 'ASTREA: Introducing Agentic Intelligence for Orbital Thermal Autonomy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alejandro D. Mousist

**分类**: cs.RO, cs.AI, cs.LG, cs.MA, eess.SY

**发布日期**: 2025-09-16 (更新: 2025-10-11)

**备注**: Accepted for presentation at the European Space Agency's AI Start 2025 Conference (see https://atpi.eventsair.com/ai-star-2025/)

---

## 💡 一句话要点

**ASTREA：面向轨道热自主性的Agentic智能系统**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `航天器热控制` `自主系统` `大型语言模型` `强化学习` `在轨验证`

## 📋 核心要点

1. 现有航天器热控制系统自主性不足，难以应对复杂多变的空间环境，依赖人工干预。
2. ASTREA采用LLM agent与强化学习控制器相结合的异步架构，实现语义推理与自适应控制的融合。
3. 在国际空间站的在轨实验验证了ASTREA的有效性，提高了热稳定性，减少了违规情况，并优化了CPU利用率。

## 📝 摘要（中文）

本文介绍了ASTREA，这是首个在飞行验证硬件（TRL 9）上执行的用于自主航天器操作的agentic系统，已在国际空间站（ISS）上进行在轨运行。以热控制作为代表性用例，我们将资源受限的大型语言模型（LLM）agent与强化学习控制器集成在一个为空间合格平台量身定制的异步架构中。地面实验表明，LLM引导的监督提高了热稳定性并减少了违规情况，证实了在硬件约束下将语义推理与自适应控制相结合的可行性。在国际空间站上的在轨验证最初面临挑战，原因是推理延迟与近地轨道（LEO）卫星的快速热循环不匹配。与轨道长度同步后，成功超越了基线，减少了违规情况，延长了episode持续时间，并提高了CPU利用率。这些发现证明了未来自主航天器中可扩展的agentic监督架构的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决航天器热控制自主性不足的问题。现有方法通常依赖预定义的规则或简单的控制算法，难以适应复杂的空间环境变化，需要大量的人工干预和优化。这限制了航天器的运行效率和任务灵活性。

**核心思路**：论文的核心思路是将大型语言模型（LLM）的语义推理能力与强化学习控制器的自适应控制能力相结合。LLM负责理解环境状态和任务目标，并生成高级控制策略；强化学习控制器则负责执行这些策略，并根据实际情况进行调整。这种结合使得系统能够更好地应对复杂和不确定的环境。

**技术框架**：ASTREA的整体架构是一个异步系统，包含以下主要模块：1) 环境感知模块，负责收集航天器的热状态数据；2) LLM agent，负责根据环境状态和任务目标生成控制策略；3) 强化学习控制器，负责执行LLM agent生成的控制策略，并根据实际情况进行调整；4) 资源管理模块，负责监控和管理系统的计算资源。这些模块以异步方式运行，以提高系统的效率和鲁棒性。

**关键创新**：ASTREA的关键创新在于将LLM agent引入到航天器热控制系统中，利用LLM的语义推理能力来指导强化学习控制器的训练和执行。与传统的基于规则或简单控制算法的方法相比，ASTREA能够更好地理解环境状态和任务目标，并生成更有效的控制策略。此外，ASTREA的异步架构也提高了系统的效率和鲁棒性。

**关键设计**：ASTREA的关键设计包括：1) 针对资源受限的航天器平台，对LLM进行了轻量化处理；2) 设计了一种有效的LLM agent与强化学习控制器之间的通信机制；3) 采用了一种基于轨道长度的同步策略，以解决推理延迟与快速热循环不匹配的问题。

## 📊 实验亮点

ASTREA在国际空间站的在轨实验中，通过与轨道长度同步，成功超越了基线系统，减少了违规情况，延长了episode持续时间，并提高了CPU利用率。这些结果表明，ASTREA能够有效地提高航天器热控制系统的自主性和性能，验证了agentic监督架构在航天领域的潜力。

## 🎯 应用场景

ASTREA技术可应用于各类航天器的自主运行与控制，例如卫星姿态控制、电源管理、故障诊断与恢复等。该研究成果有助于降低航天器运行成本，提高任务执行效率和可靠性，并为未来深空探测任务提供更强大的自主能力。此外，该技术思路也可推广到其他资源受限的嵌入式系统，例如无人机、机器人等。

## 📄 摘要（原文）

> This paper presents ASTREA, the first agentic system executed on flight-heritage hardware (TRL 9) for autonomous spacecraft operations, with on-orbit operation aboard the International Space Station (ISS). Using thermal control as a representative use case, we integrate a resource-constrained Large Language Model (LLM) agent with a reinforcement learning controller in an asynchronous architecture tailored for space-qualified platforms. Ground experiments show that LLM-guided supervision improves thermal stability and reduces violations, confirming the feasibility of combining semantic reasoning with adaptive control under hardware constraints. On-orbit validation aboard the ISS initially faced challenges due to inference latency misaligned with the rapid thermal cycles of Low Earth Orbit (LEO) satellites. Synchronization with the orbit length successfully surpassed the baseline with reduced violations, extended episode durations, and improved CPU utilization. These findings demonstrate the potential for scalable agentic supervision architectures in future autonomous spacecraft.

