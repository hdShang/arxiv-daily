---
layout: default
title: Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning
---

# Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning

**arXiv**: [2512.14057v1](https://arxiv.org/abs/2512.14057) | [PDF](https://arxiv.org/pdf/2512.14057.pdf)

**作者**: Amir M. Soufi Enayati, Homayoun Honari, Homayoun Najjaran

**分类**: cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出CRAFT模型，通过无动作Transformer编码器-解码器实现任务表示，以解决元强化学习中任务推断与策略优化的耦合问题。**

**关键词**: `元强化学习` `任务表示学习` `Transformer编码器-解码器` `无动作推断` `机器人控制` `泛化能力` `信念模型` `摊销变分推断`

## 📋 核心要点

1. 现有元强化学习方法依赖动作信息进行任务推断，导致任务表示与策略优化紧密耦合，限制了泛化能力。
2. CRAFT模型仅使用状态和奖励序列，通过Transformer编码器-解码器推断任务表示，实现任务推断与策略优化的解耦。
3. 在MetaWorld ML-10基准上，CRAFT相比基线方法展现出更快的适应速度、更好的泛化性能和更有效的探索能力。

## 📝 摘要（中文）

强化学习（RL）使机器人能在不确定环境中操作，但标准方法常难以泛化到未见任务。上下文自适应元强化学习通过任务表示来应对这些限制，但它们大多依赖经验中的完整动作信息，使任务推断与特定策略紧密耦合。本文介绍了Context Representation via Action Free Transformer encoder decoder（CRAFT），这是一种信念模型，仅从状态和奖励序列推断任务表示。通过消除对动作的依赖，CRAFT将任务推断与策略优化解耦，支持模块化训练，并利用摊销变分推断进行可扩展的信念更新。该模型基于带有旋转位置嵌入的Transformer编码器-解码器构建，能捕捉长程时间依赖，并稳健编码参数化和非参数化任务变化。在MetaWorld ML-10机器人操作基准上的实验表明，与上下文自适应元RL基线相比，CRAFT实现了更快的适应、更好的泛化和更有效的探索。这些发现突显了无动作推断作为机器人控制中可扩展RL基础的潜力。

## 🔬 方法详解

CRAFT的整体框架是一个基于Transformer编码器-解码器的信念模型，用于从状态和奖励序列推断任务表示。关键技术创新包括：采用无动作输入设计，仅依赖状态和奖励序列；使用旋转位置嵌入增强位置编码能力；结合摊销变分推断进行可扩展的信念更新。与现有方法的主要区别在于，传统上下文自适应元RL方法需要完整动作信息，而CRAFT通过移除动作依赖，实现了任务推断与策略优化的解耦，支持模块化训练，并能处理参数化和非参数化任务变化。

## 📊 实验亮点

在MetaWorld ML-10机器人操作基准实验中，CRAFT相比上下文自适应元RL基线方法，实现了更快的任务适应速度、更高的泛化性能（提升具体数值未知），以及更有效的探索策略，突显了无动作推断在提升元强化学习可扩展性和效率方面的优势。

## 🎯 应用场景

该研究主要应用于机器人控制领域，特别是在需要快速适应新任务和泛化到未见场景的元强化学习环境中。潜在应用包括工业自动化、服务机器人、自动驾驶等，其中机器人需在动态和不确定环境中高效学习和操作。

## 📄 摘要（原文）

> Reinforcement learning (RL) enables robots to operate in uncertain environments, but standard approaches often struggle with poor generalization to unseen tasks. Context-adaptive meta reinforcement learning addresses these limitations by conditioning on the task representation, yet they mostly rely on complete action information in the experience making task inference tightly coupled to a specific policy. This paper introduces Context Representation via Action Free Transformer encoder decoder (CRAFT), a belief model that infers task representations solely from sequences of states and rewards. By removing the dependence on actions, CRAFT decouples task inference from policy optimization, supports modular training, and leverages amortized variational inference for scalable belief updates. Built on a transformer encoder decoder with rotary positional embeddings, the model captures long range temporal dependencies and robustly encodes both parametric and non-parametric task variations. Experiments on the MetaWorld ML-10 robotic manipulation benchmark show that CRAFT achieves faster adaptation, improved generalization, and more effective exploration compared to context adaptive meta--RL baselines. These findings highlight the potential of action-free inference as a foundation for scalable RL in robotic control.

