---
layout: default
title: "First Plan Then Evaluate: Use a Vectorized Motion Planner for Grasping"
---

# First Plan Then Evaluate: Use a Vectorized Motion Planner for Grasping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07162" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07162v1</a>
  <a href="https://arxiv.org/pdf/2509.07162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07162v1', 'First Plan Then Evaluate: Use a Vectorized Motion Planner for Grasping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martin Matak, Mohanraj Devendran Shanthi, Karl Van Wyk, Tucker Hermans

**分类**: cs.RO

**发布日期**: 2025-09-08

---

## 💡 一句话要点

**提出基于向量化运动规划器的抓取框架，提升多指抓取的效率与成功率**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人抓取` `运动规划` `多指操作` `向量化` `并行计算` `生成器-评估器-规划器` `自主操作`

## 📋 核心要点

1. 传统抓取方法依赖耗时的轨迹优化，或因运动规划精度不足导致抓取成功率降低。
2. 该论文提出一种并行规划框架，利用向量化运动规划器高效计算多个抓取目标的轨迹。
3. 实验表明，该方法在不同场景下优于传统方法，并成功泛化到真实环境。

## 📝 摘要（中文）

自主多指抓取是机器人操作中的一项基本能力。基于优化的方法表现出色，但对初始化敏感且耗时。作为替代方案，已提出生成器-评估器-规划器框架。生成器生成抓取候选，评估器对提议的抓取进行排序，运动规划器规划到最高排名抓取的轨迹。如果规划器找不到轨迹，则使用下一个最佳抓取作为目标启动新的轨迹优化，依此类推。然而，执行较低排名的抓取意味着抓取成功率较低，并且多次轨迹优化非常耗时。或者，放宽运动规划精度阈值可以更容易地计算出成功的轨迹，但意味着在估计抓取成功可能性方面的准确性较低。这是一种双输局面：要么花费更多时间寻找成功的轨迹，要么对抓取成功的估计更差。我们提出了一个框架，该框架并行地规划到一组生成的抓取目标的轨迹，评估器估计所得轨迹的抓取成功可能性，并且机器人执行最有可能成功的轨迹。为了有效地规划到不同目标的轨迹，我们建议使用向量化运动规划器。我们的实验表明，我们的方法在不同的对象、生成器和运动规划器上都优于传统的生成器-评估器-规划器框架，并且成功地推广到现实世界中的新环境，包括不同的货架和桌子高度。

## 🔬 方法详解

**问题定义**：现有基于生成器-评估器-规划器的抓取框架，在运动规划阶段面临两难选择：要么花费大量时间进行轨迹优化以保证抓取质量，要么降低运动规划精度以加快速度，但会牺牲抓取成功率。核心问题在于如何高效地找到高质量的抓取轨迹。

**核心思路**：该论文的核心思路是并行地规划多个抓取目标的轨迹，并使用评估器估计每个轨迹的抓取成功可能性，然后选择最有可能成功的轨迹执行。通过并行规划，避免了传统方法中串行优化导致的耗时问题。

**技术框架**：整体框架包含三个主要模块：抓取候选生成器、向量化运动规划器和抓取评估器。首先，生成器生成多个抓取候选。然后，向量化运动规划器并行地为每个抓取候选规划轨迹。最后，评估器评估每个轨迹的抓取成功可能性，并选择具有最高成功可能性的轨迹执行。

**关键创新**：最重要的技术创新点是使用向量化运动规划器，能够并行地规划多个抓取目标的轨迹，显著提高了运动规划的效率。与传统方法中串行优化单个抓取目标不同，该方法能够同时考虑多个候选抓取，从而更快地找到高质量的抓取轨迹。

**关键设计**：论文中使用了特定的运动规划算法（具体算法未知），并将其向量化以支持并行计算。抓取评估器可能使用了机器学习模型，根据轨迹的特征（例如，轨迹长度、碰撞次数等）来预测抓取成功率。具体参数设置和损失函数等细节在论文中未详细说明（未知）。

## 📊 实验亮点

实验结果表明，该方法在不同对象、生成器和运动规划器上都优于传统的生成器-评估器-规划器框架。该方法能够成功泛化到真实世界中的新环境，包括不同的货架和桌子高度，验证了其在实际应用中的可行性和鲁棒性。具体的性能提升数据在摘要中未提及（未知）。

## 🎯 应用场景

该研究成果可应用于各种机器人操作场景，例如工业自动化、物流分拣、家庭服务机器人等。通过提高抓取的效率和成功率，可以显著提升机器人的自主操作能力，使其能够更好地适应复杂和动态的环境。未来，该技术有望在智能制造、智慧物流等领域发挥重要作用。

## 📄 摘要（原文）

> Autonomous multi-finger grasping is a fundamental capability in robotic manipulation. Optimization-based approaches show strong performance, but tend to be sensitive to initialization and are potentially time-consuming. As an alternative, the generator-evaluator-planner framework has been proposed. A generator generates grasp candidates, an evaluator ranks the proposed grasps, and a motion planner plans a trajectory to the highest-ranked grasp. If the planner doesn't find a trajectory, a new trajectory optimization is started with the next-best grasp as the target and so on. However, executing lower-ranked grasps means a lower chance of grasp success, and multiple trajectory optimizations are time-consuming. Alternatively, relaxing the threshold for motion planning accuracy allows for easier computation of a successful trajectory but implies lower accuracy in estimating grasp success likelihood. It's a lose-lose proposition: either spend more time finding a successful trajectory or have a worse estimate of grasp success. We propose a framework that plans trajectories to a set of generated grasp targets in parallel, the evaluator estimates the grasp success likelihood of the resulting trajectories, and the robot executes the trajectory most likely to succeed. To plan trajectories to different targets efficiently, we propose the use of a vectorized motion planner. Our experiments show our approach improves over the traditional generator-evaluator-planner framework across different objects, generators, and motion planners, and successfully generalizes to novel environments in the real world, including different shelves and table heights. Project website https://sites.google.com/view/fpte

