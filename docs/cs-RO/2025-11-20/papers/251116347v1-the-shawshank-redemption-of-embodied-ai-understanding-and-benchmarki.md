---
layout: default
title: The Shawshank Redemption of Embodied AI: Understanding and Benchmarking Indirect Environmental Jailbreaks
---

# The Shawshank Redemption of Embodied AI: Understanding and Benchmarking Indirect Environmental Jailbreaks

**arXiv**: [2511.16347v1](https://arxiv.org/abs/2511.16347) | [PDF](https://arxiv.org/pdf/2511.16347.pdf)

**作者**: Chunyang Li, Zifeng Kang, Junwei Zhang, Zhuo Ma, Anda Cheng, Xinghua Li, Jianfeng Ma

---

## 💡 一句话要点

**提出间接环境越狱攻击与自动框架，以评估具身AI安全风险。**

**关键词**: `具身AI安全` `间接越狱攻击` `视觉语言模型` `自动基准生成` `多模态提示注入`

## 📋 核心要点

1. 核心问题：具身AI对环境的盲目信任易被利用，导致间接越狱攻击。
2. 方法要点：设计SHAWSHANK自动攻击生成和SHAWSHANK-FORGE基准生成框架。
3. 实验或效果：在3957个任务场景中优于11种方法，攻破所有测试VLM。

## 📄 摘要（原文）

> The adoption of Vision-Language Models (VLMs) in embodied AI agents, while being effective, brings safety concerns such as jailbreaking. Prior work have explored the possibility of directly jailbreaking the embodied agents through elaborated multi-modal prompts. However, no prior work has studied or even reported indirect jailbreaks in embodied AI, where a black-box attacker induces a jailbreak without issuing direct prompts to the embodied agent. In this paper, we propose, for the first time, indirect environmental jailbreak (IEJ), a novel attack to jailbreak embodied AI via indirect prompt injected into the environment, such as malicious instructions written on a wall. Our key insight is that embodied AI does not ''think twice'' about the instructions provided by the environment -- a blind trust that attackers can exploit to jailbreak the embodied agent. We further design and implement open-source prototypes of two fully-automated frameworks: SHAWSHANK, the first automatic attack generation framework for the proposed attack IEJ; and SHAWSHANK-FORGE, the first automatic benchmark generation framework for IEJ. Then, using SHAWSHANK-FORGE, we automatically construct SHAWSHANK-BENCH, the first benchmark for indirectly jailbreaking embodied agents. Together, our two frameworks and one benchmark answer the questions of what content can be used for malicious IEJ instructions, where they should be placed, and how IEJ can be systematically evaluated. Evaluation results show that SHAWSHANK outperforms eleven existing methods across 3,957 task-scene combinations and compromises all six tested VLMs. Furthermore, current defenses only partially mitigate our attack, and we have responsibly disclosed our findings to all affected VLM vendors.

