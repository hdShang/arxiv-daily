---
layout: default
title: Beyond Master and Apprentice: Grounding Foundation Models for Symbiotic Interactive Learning in a Shared Latent Space
---

# Beyond Master and Apprentice: Grounding Foundation Models for Symbiotic Interactive Learning in a Shared Latent Space

**arXiv**: [2511.05203v1](https://arxiv.org/abs/2511.05203) | [PDF](https://arxiv.org/pdf/2511.05203.pdf)

**作者**: Linus Nwankwo, Björn Ellensohn, Christian Rauch, Elmar Rueckert

---

## 💡 一句话要点

**提出共生交互学习方法，在共享潜在空间中实现人机双向共同适应。**

**关键词**: `共生交互学习` `共享潜在空间` `人机交互` `基础模型` `共同适应` `任务表示`

## 📋 核心要点

1. 当前人机交互沿用主从模式，缺乏双向共同适应。
2. 方法在共享潜在任务空间中实现联合信念状态演化，支持主动澄清和计划优化。
3. 在模拟和真实任务中验证，包括指令跟随和交互对话。

## 📄 摘要（原文）

> Today's autonomous agents can understand free-form natural language
> instructions and execute long-horizon tasks in a manner akin to human-level
> reasoning. These capabilities are mostly driven by large-scale pre-trained
> foundation models (FMs). However, the approaches with which these models are
> grounded for human-robot interaction (HRI) perpetuate a master-apprentice
> model, where the apprentice (embodied agent) passively receives and executes
> the master's (human's) commands without reciprocal learning. This reactive
> interaction approach does not capture the co-adaptive dynamics inherent in
> everyday multi-turn human-human interactions. To address this, we propose a
> Symbiotic Interactive Learning (SIL) approach that enables both the master and
> the apprentice to co-adapt through mutual, bidirectional interactions. We
> formalised SIL as a co-adaptation process within a shared latent task space,
> where the agent and human maintain joint belief states that evolve based on
> interaction history. This enables the agent to move beyond reactive execution
> to proactive clarification, adaptive suggestions, and shared plan refinement.
> To realise these novel behaviours, we leveraged pre-trained FMs for spatial
> perception and reasoning, alongside a lightweight latent encoder that grounds
> the models' outputs into task-specific representations. Furthermore, to ensure
> stability as the tasks evolve, we augment SIL with a memory architecture that
> prevents the forgetting of learned task-space representations. We validate SIL
> on both simulated and real-world embodied tasks, including instruction
> following, information retrieval, query-oriented reasoning, and interactive
> dialogues. Demos and resources are public
> at:~\href{https://linusnep.github.io/SIL/}{https://linusnep.github.io/SIL/}.

