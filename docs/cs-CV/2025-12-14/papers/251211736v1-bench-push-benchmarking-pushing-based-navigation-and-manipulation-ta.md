---
layout: default
title: Bench-Push: Benchmarking Pushing-based Navigation and Manipulation Tasks for Mobile Robots
---

# Bench-Push: Benchmarking Pushing-based Navigation and Manipulation Tasks for Mobile Robots

**arXiv**: [2512.11736v1](https://arxiv.org/abs/2512.11736) | [PDF](https://arxiv.org/pdf/2512.11736.pdf)

**作者**: Ninghan Zhong, Steven Caro, Megnath Ramesh, Rishi Bhatnagar, Avraiem Iskandar, Stephen L. Smith

---

## 💡 一句话要点

**提出Bench-Push基准以解决移动机器人在杂乱环境中基于推动的导航与操作任务评估问题**

**关键词**: `移动机器人` `推动操作` `基准测试` `导航任务` `模拟环境` `开源库`

## 📋 核心要点

1. 核心问题：移动机器人在杂乱环境中需推动物体，但现有评估方法依赖临时设置，缺乏可重复性和跨比较性。
2. 方法要点：提供统一基准，包括模拟环境、评估指标和开源Python库，支持推动任务的标准化测试。
3. 实验或效果：通过示例实现评估基线方法，涵盖迷宫导航、冰区航行等任务，并开源代码和模型。

## 📄 摘要（原文）

> Mobile robots are increasingly deployed in cluttered environments with movable objects, posing challenges for traditional methods that prohibit interaction. In such settings, the mobile robot must go beyond traditional obstacle avoidance, leveraging pushing or nudging strategies to accomplish its goals. While research in pushing-based robotics is growing, evaluations rely on ad hoc setups, limiting reproducibility and cross-comparison. To address this, we present Bench-Push, the first unified benchmark for pushing-based mobile robot navigation and manipulation tasks. Bench-Push includes multiple components: 1) a comprehensive range of simulated environments that capture the fundamental challenges in pushing-based tasks, including navigating a maze with movable obstacles, autonomous ship navigation in ice-covered waters, box delivery, and area clearing, each with varying levels of complexity; 2) novel evaluation metrics to capture efficiency, interaction effort, and partial task completion; and 3) demonstrations using Bench-Push to evaluate example implementations of established baselines across environments. Bench-Push is open-sourced as a Python library with a modular design. The code, documentation, and trained models can be found at https://github.com/IvanIZ/BenchNPIN.

