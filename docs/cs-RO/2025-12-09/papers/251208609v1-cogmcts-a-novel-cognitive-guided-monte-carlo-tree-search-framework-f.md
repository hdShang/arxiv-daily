---
layout: default
title: CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models
---

# CogMCTS: A Novel Cognitive-Guided Monte Carlo Tree Search Framework for Iterative Heuristic Evolution with Large Language Models

**arXiv**: [2512.08609v1](https://arxiv.org/abs/2512.08609) | [PDF](https://arxiv.org/pdf/2512.08609.pdf)

**作者**: Hui Wang, Yang Liu, Xiaoyu Zhang, Chaoxu Mu

---

## 💡 一句话要点

**提出CogMCTS框架，结合认知引导与MCTS以优化基于LLM的自动启发式设计**

**关键词**: `自动启发式设计` `蒙特卡洛树搜索` `大语言模型` `认知引导` `启发式优化`

## 📋 核心要点

1. 现有LLM进化方法易陷局部最优，MCTS集成中认知整合与搜索多样性受限
2. CogMCTS通过多轮认知反馈、双轨节点扩展和策略突变，动态改进启发式生成
3. 实验表明CogMCTS在稳定性、效率和解决方案质量上优于现有方法

## 📄 摘要（原文）

> Automatic Heuristic Design (AHD) is an effective1 framework for solving complex optimization prob-2 lems. The development of large language mod-3 els (LLMs) enables the automated generation of4 heuristics. Existing LLM-based evolutionary meth-5 ods rely on population strategies and are prone6 to local optima. Integrating LLMs with Monte7 Carlo Tree Search (MCTS) improves the trade-off8 between exploration and exploitation, but multi-9 round cognitive integration remains limited and10 search diversity is constrained. To overcome these11 limitations, this paper proposes a novel cognitive-12 guided MCTS framework (CogMCTS). CogMCTS13 tightly integrates the cognitive guidance mecha-14 nism of LLMs with MCTS to achieve efficient au-15 tomated heuristic optimization. The framework16 employs multi-round cognitive feedback to incor-17 porate historical experience, node information, and18 negative outcomes, dynamically improving heuris-19 tic generation. Dual-track node expansion com-20 bined with elite heuristic management balances the21 exploration of diverse heuristics and the exploita-22 tion of high-quality experience. In addition, strate-23 gic mutation modifies the heuristic forms and pa-24 rameters to further enhance the diversity of the so-25 lution and the overall optimization performance.26 The experimental results indicate that CogMCTS27 outperforms existing LLM-based AHD methods in28 stability, efficiency, and solution quality.

