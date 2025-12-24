---
layout: default
title: "Self-Augmented Robot Trajectory: Efficient Imitation Learning via Safe Self-augmentation with Demonstrator-annotated Precision"
---

# Self-Augmented Robot Trajectory: Efficient Imitation Learning via Safe Self-augmentation with Demonstrator-annotated Precision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09893" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09893v1</a>
  <a href="https://arxiv.org/pdf/2509.09893.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09893v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09893v1', 'Self-Augmented Robot Trajectory: Efficient Imitation Learning via Safe Self-augmentation with Demonstrator-annotated Precision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanbit Oh, Masaki Murooka, Tomohiro Motoda, Ryoichi Nakajo, Yukiyasu Domae

**分类**: cs.RO, cs.AI

**发布日期**: 2025-09-11

**备注**: Under review

---

## 💡 一句话要点

**SART：通过安全自增强的机器人轨迹学习，提升模仿学习效率**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `模仿学习` `机器人轨迹` `数据增强` `安全探索` `机器人操作`

## 📋 核心要点

1. 传统模仿学习依赖大量人工演示或随机探索，数据收集成本高昂，尤其在安全要求高的任务中。
2. SART框架通过单次人工演示和后续的机器人自主安全增强，有效扩展数据集，提升学习效率。
3. 实验结果表明，SART在模拟和真实机器人操作任务中，显著提高了策略的成功率，验证了其有效性。

## 📝 摘要（中文）

模仿学习是训练机器人智能体的有效范式。然而，标准方法通常需要大量数据，通过多次演示或随机探索来确保可靠性能。虽然探索减少了人工干预，但缺乏安全保证，容易发生碰撞，尤其是在间隙受限的任务中（如插孔）。这需要手动重置环境，增加人工负担。本研究提出了自增强机器人轨迹（SART）框架，仅需单次人工演示即可进行策略学习，并通过自主增强安全地扩展数据集。SART包含两个阶段：（1）单次人工示教，提供一次演示，并标注关键路径点周围的精度边界（表示为球体），然后重置一次环境；（2）机器人自增强，机器人在这些边界内生成多样且无碰撞的轨迹，并重新连接到原始演示。这种设计通过最小化人工干预来提高数据收集效率，同时确保安全。在模拟和真实操作任务中的大量评估表明，SART比仅在人工收集的演示上训练的策略实现了更高的成功率。

## 🔬 方法详解

**问题定义**：论文旨在解决模仿学习中数据效率低下的问题，尤其是在机器人操作任务中，传统方法需要大量人工演示或不安全的随机探索。人工演示成本高，而随机探索可能导致碰撞，需要频繁的人工干预重置环境，增加了学习难度和时间成本。

**核心思路**：论文的核心思路是利用单次人工演示作为基础，通过机器人自主生成安全且多样化的轨迹来扩充数据集。关键在于限制机器人探索的范围，使其在人工演示的关键路径点附近进行安全探索，避免碰撞，同时保证生成轨迹的多样性，从而提高策略学习的泛化能力。

**技术框架**：SART框架包含两个主要阶段：1) 人工示教阶段：人工提供一次演示轨迹，并对关键路径点进行标注，确定精度边界（球体）。2) 机器人自增强阶段：机器人根据人工示教的精度边界，生成多样且无碰撞的轨迹，并将这些轨迹重新连接到原始演示轨迹上，从而扩充数据集。

**关键创新**：SART的关键创新在于提出了一个安全自增强的框架，它结合了人工示教的引导性和机器人自主探索的效率。通过人工标注的精度边界，限制了机器人的探索空间，保证了安全性，同时允许机器人在边界内生成多样化的轨迹，提高了数据效率。与传统方法相比，SART显著减少了人工干预的需求，并提高了学习的安全性。

**关键设计**：精度边界的设计是关键。论文使用球体来表示关键路径点周围的精度范围，球体的大小可以根据任务的精度要求进行调整。机器人生成轨迹时，需要保证轨迹在球体内部，并且与原始演示轨迹平滑连接。具体的轨迹生成方法可能涉及运动规划算法或优化方法，以确保轨迹的平滑性和无碰撞性。损失函数的设计可能包括轨迹的平滑性损失、与原始演示轨迹的相似性损失等。

## 📊 实验亮点

论文在模拟和真实机器人操作任务中进行了评估，结果表明SART显著提高了策略的成功率。例如，在插孔任务中，SART仅使用单次人工演示即可达到远高于仅使用人工演示训练的策略的成功率。具体的性能数据和对比基线在论文中有详细描述，证明了SART在数据效率和安全性方面的优势。

## 🎯 应用场景

SART框架可应用于各种需要高精度和安全性的机器人操作任务，例如装配、焊接、医疗手术等。通过减少人工示教的需求，降低了机器人部署的成本和难度。该方法还可以应用于其他需要安全探索的强化学习任务，例如自动驾驶、无人机导航等，具有广泛的应用前景。

## 📄 摘要（原文）

> Imitation learning is a promising paradigm for training robot agents; however, standard approaches typically require substantial data acquisition -- via numerous demonstrations or random exploration -- to ensure reliable performance. Although exploration reduces human effort, it lacks safety guarantees and often results in frequent collisions -- particularly in clearance-limited tasks (e.g., peg-in-hole) -- thereby, necessitating manual environmental resets and imposing additional human burden. This study proposes Self-Augmented Robot Trajectory (SART), a framework that enables policy learning from a single human demonstration, while safely expanding the dataset through autonomous augmentation. SART consists of two stages: (1) human teaching only once, where a single demonstration is provided and precision boundaries -- represented as spheres around key waypoints -- are annotated, followed by one environment reset; (2) robot self-augmentation, where the robot generates diverse, collision-free trajectories within these boundaries and reconnects to the original demonstration. This design improves the data collection efficiency by minimizing human effort while ensuring safety. Extensive evaluations in simulation and real-world manipulation tasks show that SART achieves substantially higher success rates than policies trained solely on human-collected demonstrations. Video results available at https://sites.google.com/view/sart-il .

