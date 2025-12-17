---
layout: default
title: AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation
---

# AsymPuzl: An Asymmetric Puzzle for multi-agent cooperation

**arXiv**: [2512.03466v1](https://arxiv.org/abs/2512.03466) | [PDF](https://arxiv.org/pdf/2512.03466.pdf)

**作者**: Xavier Cadet, Edward Koh, Peter Chin

---

## 💡 一句话要点

**提出AsymPuzl以评估信息不对称下多智能体合作中的通信策略**

**关键词**: `多智能体合作` `信息不对称` `通信策略` `LLM评估` `反馈机制` `合作拼图`

## 📋 核心要点

1. 核心问题：现有多智能体场景多关注开放角色扮演，缺乏受控评估信息不对称下的通信能力
2. 方法要点：设计最小化但表达性强的双智能体拼图环境，智能体观察互补不完整视图，需交换消息合作解决
3. 实验或效果：使用多种LLM测试，强模型可靠收敛，弱模型忽略消息或过度修正，反馈设计影响性能

## 📄 摘要（原文）

> Large Language Model (LLM) agents are increasingly studied in multi-turn, multi-agent scenarios, yet most existing setups emphasize open-ended role-play rather than controlled evaluation. We introduce AsymPuzl, a minimal but expressive two-agent puzzle environment designed to isolate communication under information asymmetry. Each agent observes complementary but incomplete views of a symbolic puzzle and must exchange messages to solve it cooperatively. Using a diverse set of current-generation and open-source LLMs, we show that (i) strong models such as GPT-5 and Claude-4.0 reliably converge across puzzle sizes on the solution by sharing complete information in two turns, (ii) weaker models often ignore partner messages or over-correct their hypotheses, and (iii) feedback design is non-trivial: simple self-feedback improves success rates, while detailed joint feedback can hurt performance. These findings show that even in simple cooperative tasks, LLM communication strategies diverge and depend on the granularity of feedback signals. AsymPuzl thus provides a testbed for probing the limits of multi-turn cooperation and opens avenues for studying coordination mechanisms.

