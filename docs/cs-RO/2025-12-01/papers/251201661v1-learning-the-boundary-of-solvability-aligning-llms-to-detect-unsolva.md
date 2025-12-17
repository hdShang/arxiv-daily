---
layout: default
title: Learning the Boundary of Solvability: Aligning LLMs to Detect Unsolvable Problems
---

# Learning the Boundary of Solvability: Aligning LLMs to Detect Unsolvable Problems

**arXiv**: [2512.01661v1](https://arxiv.org/abs/2512.01661) | [PDF](https://arxiv.org/pdf/2512.01661.pdf)

**作者**: Dengyun Peng, Qiguang Chen, Bofei Liu, Jiannan Guan, Libo Qin, Zheng Yan, Jinhao Liu, Jianshu Zhang, Wanxiang Che

---

## 💡 一句话要点

**提出UnsolvableQA和UnsolvableRL以解决LLM在检测不可解问题时的可靠性问题**

**关键词**: `不可解问题检测` `LLM可靠性` `强化学习框架` `数据集构建` `能力崩溃`

## 📋 核心要点

1. 核心问题：LLM难以区分客观不可解（问题内在矛盾）与主观能力限制（模型能力不足），导致幻觉和过度自信。
2. 方法要点：构建UnsolvableQA数据集，包含可解和不可解实例，并基于此设计UnsolvableRL强化学习框架，结合准确性、不可解性和难度奖励。
3. 实验或效果：方法实现近乎完美的不可解检测，同时提升可解任务准确性，并发现能力崩溃现象，强调暴露不可解数据的必要性。

## 📄 摘要（原文）

> Ensuring LLM reliability requires not only solving complex problems but also recognizing when a problem is unsolvable. Current models often struggle to distinguish objective unsolvability (inherent contradictions in the problem) from subjective capability limitations (problems beyond the model's competence), which leads to hallucinations and overconfidence. To address this, we propose UnsolvableQA and UnsolvableRL to solve feasible problems, detect inherent contradictions, and prudently refuse tasks beyond capability. Specifically, we construct UnsolvableQA, a dataset of paired solvable and unsolvable instances derived via a dual-track methodology: programmatic generation for logic puzzles and a novel "Reverse Construction" method that injects contradictions into valid reasoning chains for mathematics. Building on this dataset, we introduce UnsolvableRL, a reinforcement learning framework with three reward components jointly accounting for accuracy, unsolvability, and difficulty. Empirical results show that our approach achieves near-perfect unsolvability detection while also improving accuracy on solvable tasks. Crucially, we identify Capability Collapse, demonstrating that explicit exposure to unsolvable data is indispensable for preventing models from becoming systematically overconfident. Our code and data are available at https://github.com/sfasfaffa/unsolvableQA.

