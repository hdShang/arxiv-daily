---
layout: default
title: "Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining"
---

# Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16475" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16475v2</a>
  <a href="https://arxiv.org/pdf/2506.16475.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16475v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16475v2', 'Human2LocoMan: Learning Versatile Quadrupedal Manipulation with Human Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaru Niu, Yunzhe Zhang, Mingyang Yu, Changyi Lin, Chenhao Li, Yikai Wang, Yuxiang Yang, Wenhao Yu, Tingnan Zhang, Zhenzhen Li, Jonathan Francis, Bingqing Chen, Jie Tan, Ding Zhao

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-19 (更新: 2025-07-07)

---

## 💡 一句话要点

**提出跨体现模仿学习系统以解决四足机器人操控能力不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `四足机器人` `模仿学习` `操控能力` `数据集构建` `跨体现学习` `遥操作` `家庭任务`

## 📋 核心要点

1. 现有的四足机器人在复杂环境中的操控能力不足，缺乏有效的自主操控技能，限制了其应用范围。
2. 本研究提出了一种跨体现模仿学习系统，利用人类和机器人数据的结合，构建了统一的观察与动作空间。
3. 实验结果显示，该系统在六个真实世界操控任务中，整体成功率提升41.9%，在OOD设置下提升79.7%。

## 📝 摘要（中文）

四足机器人在复杂环境中的运动能力令人印象深刻，但在可扩展性方面实现自主多功能操控技能仍然是一个重大挑战。本研究提出了一种跨体现模仿学习系统，利用从人类和LocoMan（一个配备多种操控模式的四足机器人）收集的数据。我们开发了一个统一和模块化的人机观察与动作空间的遥操作和数据收集管道。为有效利用收集的数据，我们提出了一种高效的模块化架构，支持不同体现间的结构化模态对齐数据的共同训练和预训练。此外，我们构建了第一个LocoMan机器人操控数据集，涵盖多种家庭任务，并验证了系统在六个真实世界操控任务中的有效性，整体成功率提升41.9%。

## 🔬 方法详解

**问题定义**：本研究旨在解决四足机器人在复杂环境中自主操控能力不足的问题。现有方法在操控技能的可扩展性和有效性上存在显著不足，限制了机器人的应用潜力。

**核心思路**：论文提出了一种跨体现模仿学习系统，通过结合人类和LocoMan机器人的数据，构建统一的观察与动作空间，从而提升机器人的操控能力。

**技术框架**：整体架构包括遥操作和数据收集管道，模块化设计使得人类与机器人之间的观察和动作空间得以统一。系统支持不同体现间的共同训练和预训练，提升了数据利用效率。

**关键创新**：本研究的创新点在于首次构建了LocoMan机器人操控数据集，并提出了高效的模块化架构，支持跨体现的数据对齐与训练，显著提升了操控技能的学习效率。

**关键设计**：在设计上，采用了模块化的网络结构，优化了损失函数以适应不同操控任务的需求，确保了在仅使用一半机器人数据的情况下，仍能实现显著的性能提升。

## 📊 实验亮点

实验结果表明，所提出的系统在六个真实世界操控任务中，整体成功率提升41.9%，在OOD设置下成功率提升达79.7%。预训练使用人类数据的情况下，成功率提升38.6%，在OOD设置下更是达到82.7%。

## 🎯 应用场景

该研究的潜在应用领域包括家庭服务机器人、工业自动化和救援任务等。通过提升四足机器人的操控能力，能够更好地完成复杂的任务，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Quadrupedal robots have demonstrated impressive locomotion capabilities in complex environments, but equipping them with autonomous versatile manipulation skills in a scalable way remains a significant challenge. In this work, we introduce a cross-embodiment imitation learning system for quadrupedal manipulation, leveraging data collected from both humans and LocoMan, a quadruped equipped with multiple manipulation modes. Specifically, we develop a teleoperation and data collection pipeline, which unifies and modularizes the observation and action spaces of the human and the robot. To effectively leverage the collected data, we propose an efficient modularized architecture that supports co-training and pretraining on structured modality-aligned data across different embodiments. Additionally, we construct the first manipulation dataset for the LocoMan robot, covering various household tasks in both unimanual and bimanual modes, supplemented by a corresponding human dataset. We validate our system on six real-world manipulation tasks, where it achieves an average success rate improvement of 41.9% overall and 79.7% under out-of-distribution (OOD) settings compared to the baseline. Pretraining with human data contributes a 38.6% success rate improvement overall and 82.7% under OOD settings, enabling consistently better performance with only half the amount of robot data. Our code, hardware, and data are open-sourced at: https://human2bots.github.io.

