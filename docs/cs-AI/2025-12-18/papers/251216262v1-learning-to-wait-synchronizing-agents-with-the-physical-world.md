---
layout: default
title: Learning to Wait: Synchronizing Agents with the Physical World
---

# Learning to Wait: Synchronizing Agents with the Physical World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16262" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16262v1</a>
  <a href="https://arxiv.org/pdf/2512.16262.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16262v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16262v1', 'Learning to Wait: Synchronizing Agents with the Physical World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei She, Ping Zhang, He Liu, Yanmin Jia, Yang Jing, Zijun Liu, Peng Sun, Xiangbin Li, Xiaohe Hu

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Agent端时间同步方法，解决LLM在异步环境中的时序校准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Agent` `大型语言模型` `时间同步` `异步环境` `上下文学习`

## 📋 核心要点

1. 现实Agent任务中，动作完成存在时间延迟，导致Agent与环境交互出现时间间隔，现有方法难以兼顾效率与上下文完整性。
2. 论文提出Agent端时间同步方法，通过LLM预测等待时长，使Agent主动与异步环境对齐，无需频繁轮询。
3. 实验表明，该方法能有效校准Agent内部时钟，降低查询开销和执行延迟，验证了时间感知能力的可学习性。

## 📝 摘要（中文）

与同步马尔可夫决策过程（MDP）不同，现实世界的Agent任务通常涉及具有可变延迟的非阻塞动作，从而在动作发起和完成之间产生根本性的“时间间隔”。现有的环境端解决方案，如阻塞包装器或频繁轮询，要么限制了可扩展性，要么用冗余观察稀释了Agent的上下文窗口。本文提出了一种Agent端方法，使大型语言模型（LLM）能够主动将其“认知时间线”与物理世界对齐。通过将代码即动作范式扩展到时间域，Agent利用语义先验和上下文学习（ICL）来预测精确的等待时长（`time.sleep(t)`），从而有效地与异步环境同步，而无需详尽的检查。在模拟的Kubernetes集群中的实验表明，Agent可以精确地校准其内部时钟，以最大限度地减少查询开销和执行延迟，从而验证了时间感知是在开放环境中自主进化必不可少的、可学习的能力。

## 🔬 方法详解

**问题定义**：现有方法在处理现实世界Agent任务时，由于动作的非阻塞性和可变延迟，导致Agent的认知时间线与物理世界存在时间间隔。环境端的解决方案，如阻塞包装器，会限制可扩展性；频繁轮询则会稀释Agent的上下文窗口，降低效率。因此，如何使Agent在异步环境中高效、准确地与环境同步是一个关键问题。

**核心思路**：论文的核心思路是赋予Agent时间感知能力，使其能够主动预测并等待动作完成所需的时间，从而实现与异步环境的同步。通过将时间维度融入Agent的决策过程，避免了被动等待或频繁查询，提高了效率和准确性。

**技术框架**：该方法基于代码即动作范式，利用大型语言模型（LLM）作为Agent的决策核心。Agent通过观察环境状态，利用语义先验和上下文学习（ICL）来预测等待时长，并执行`time.sleep(t)`指令。整体流程包括：1) Agent观察环境；2) LLM基于上下文预测等待时间；3) Agent执行`time.sleep(t)`；4) Agent再次观察环境，循环执行。

**关键创新**：最重要的技术创新点在于将时间感知能力融入Agent的决策过程，使其能够主动预测等待时间，而不是依赖环境的同步机制。这种Agent端的时间同步方法，避免了环境端解决方案的局限性，提高了Agent在异步环境中的适应性和效率。

**关键设计**：关键设计包括：1) 使用LLM作为Agent的决策核心，利用其强大的语义理解和推理能力；2) 通过上下文学习（ICL）提供时间相关的示例，引导LLM预测准确的等待时间；3) 使用`time.sleep(t)`指令模拟等待动作完成，实现Agent与环境的时间同步；4) 在模拟的Kubernetes集群中进行实验，验证该方法在实际场景中的有效性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16262v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在模拟的Kubernetes集群中能够显著降低查询开销和执行延迟。Agent能够精确地校准其内部时钟，与异步环境实现高效同步。具体性能数据未知，但论文强调了该方法在最小化查询开销和执行延迟方面的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要与异步环境交互的Agent任务，例如机器人控制、自动化运维、智能家居等。通过赋予Agent时间感知能力，可以提高其在复杂、动态环境中的自主性和效率，实现更智能、更可靠的自动化系统。未来，该方法有望扩展到更广泛的领域，例如智能交通、金融交易等。

## 📄 摘要（原文）

> Real-world agentic tasks, unlike synchronous Markov Decision Processes (MDPs), often involve non-blocking actions with variable latencies, creating a fundamental \textit{Temporal Gap} between action initiation and completion. Existing environment-side solutions, such as blocking wrappers or frequent polling, either limit scalability or dilute the agent's context window with redundant observations. In this work, we propose an \textbf{Agent-side Approach} that empowers Large Language Models (LLMs) to actively align their \textit{Cognitive Timeline} with the physical world. By extending the Code-as-Action paradigm to the temporal domain, agents utilize semantic priors and In-Context Learning (ICL) to predict precise waiting durations (\texttt{time.sleep(t)}), effectively synchronizing with asynchronous environment without exhaustive checking. Experiments in a simulated Kubernetes cluster demonstrate that agents can precisely calibrate their internal clocks to minimize both query overhead and execution latency, validating that temporal awareness is a learnable capability essential for autonomous evolution in open-ended environments.

