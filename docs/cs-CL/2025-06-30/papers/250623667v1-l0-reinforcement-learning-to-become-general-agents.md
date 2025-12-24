---
layout: default
title: "L0: Reinforcement Learning to Become General Agents"
---

# L0: Reinforcement Learning to Become General Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23667" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23667v1</a>
  <a href="https://arxiv.org/pdf/2506.23667.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23667v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23667v1', 'L0: Reinforcement Learning to Become General Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Zhang, Jingyi Xi, Zhuoyang Song, Junyu Lu, Yuhua Ke, Ting Sun, Yukun Yang, Jiaxing Zhang, Songxin Zhang, Zejian Xie

**分类**: cs.CL

**发布日期**: 2025-06-30

**🔗 代码/项目**: [GITHUB](https://github.com/cmriat/l0)

---

## 💡 一句话要点

**提出L-Zero以解决大规模自主智能体训练效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主智能体` `强化学习` `大型语言模型` `并发训练` `可验证奖励`

## 📋 核心要点

1. 现有方法在训练大型语言模型作为自主智能体时面临可扩展性和效率的挑战，限制了其在复杂任务中的应用。
2. 论文提出L-Zero（L0），一个可扩展的端到端训练管道，结合低成本的并发智能体工作池，简化了强化学习的应用。
3. 实验结果显示，L0在多个问答基准上显著提升了模型的准确率，验证了其在问题解决能力上的有效性。

## 📝 摘要（中文）

训练大型语言模型（LLMs）作为自主智能体以应对多轮长时间任务仍面临可扩展性和训练效率的重大挑战。为此，我们提出了L-Zero（L0），一个可扩展的端到端训练管道，旨在为通用智能体提供支持。L0具有低成本、可扩展和沙箱式的并发智能体工作池，降低了在复杂环境中应用强化学习的门槛。我们还引入了NB-Agent，作为L0中的智能体框架，通过读-评-打印-循环（REPL）以“代码即行动”的方式运作。我们在事实性问答基准上评估了L0，实验表明基础模型仅通过可验证奖励的强化学习（RLVR）即可发展出稳健的问题解决能力。在Qwen2.5-7B-Instruct模型上，我们的方法使SimpleQA的准确率从30%提升至80%，HotpotQA的准确率从22%提升至41%。我们已开源整个L0系统，包括L0系列模型、NB-Agent、完整的训练管道及相应的训练配方。

## 🔬 方法详解

**问题定义**：本论文旨在解决训练大型语言模型作为自主智能体时的可扩展性和训练效率问题。现有方法在复杂环境中应用强化学习时，往往面临高成本和低效率的挑战。

**核心思路**：L-Zero（L0）通过构建一个低成本、可扩展的并发智能体工作池，降低了强化学习的应用门槛。引入的NB-Agent以“代码即行动”的方式运作，提升了智能体的灵活性和效率。

**技术框架**：L0的整体架构包括一个并发智能体工作池和NB-Agent模块。工作池负责管理多个智能体的并行训练，而NB-Agent则通过REPL机制执行代码，实时反馈和调整策略。

**关键创新**：L0的主要创新在于其并发智能体工作池的设计和NB-Agent的“代码即行动”机制。这种设计使得智能体能够在复杂环境中更高效地学习和适应。

**关键设计**：在L0中，关键参数设置包括智能体的并发数量、奖励机制的设计（可验证奖励）以及NB-Agent的代码执行效率。这些设计确保了训练过程的高效性和智能体的学习能力。

## 📊 实验亮点

实验结果显示，L0在SimpleQA基准上的准确率从30%提升至80%，在HotpotQA基准上的准确率从22%提升至41%。这些显著的提升表明L0在问题解决能力上的有效性，验证了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、自动化决策系统和复杂任务的自主执行等。通过提升大型语言模型的自主学习能力，L0能够在多种实际场景中提供更高效的解决方案，推动智能体技术的发展与应用。

## 📄 摘要（原文）

> Training large language models (LLMs) to act as autonomous agents for multi-turn, long-horizon tasks remains significant challenges in scalability and training efficiency. To address this, we introduce L-Zero (L0), a scalable, end-to-end training pipeline for general-purpose agents. Featuring a low-cost, extensible, and sandboxed concurrent agent worker pool, L0 lowers the barrier for applying reinforcement learning in complex environments. We also introduce NB-Agent, the agent scaffold within L0, which operates in a "code-as-action" fashion via a Read-Eval-Print-Loop (REPL). We evaluate L0 on factuality question-answering benchmarks. Our experiments demonstrate that a base model can develop robust problem-solving skills using solely Reinforcement Learning with Verifiable Rewards (RLVR). On the Qwen2.5-7B-Instruct model, our method boosts accuracy on SimpleQA from 30 % to 80 % and on HotpotQA from 22 % to 41 %. We have open-sourced the entire L0 system, including our L0 series models, the NB-Agent, a complete training pipeline, and the corresponding training recipes on (https://github.com/cmriat/l0).

