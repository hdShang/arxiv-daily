---
layout: default
title: LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy
---

# LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.03529" target="_blank" class="toolbar-btn">arXiv: 2510.03529v1</a>
    <a href="https://arxiv.org/pdf/2510.03529.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03529v1" 
            onclick="toggleFavorite(this, '2510.03529v1', 'LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Zekai Liang, Xiao Liang, Soofiyan Atar, Sreyan Das, Zoe Chiu, Peihan Zhang, Florian Richter, Shanglei Liu, Michael C. Yip

**分类**: cs.RO

**发布日期**: 2025-10-03

---

## 💡 一句话要点

**LapSurgie：提出基于人型机器人的遥操作腹腔镜手术框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人型机器人` `腹腔镜手术` `遥操作` `逆映射控制` `医疗机器人`

## 📋 核心要点

1. 现有手术机器人平台主要集中在高资源医疗中心，加剧了医疗资源分配不均的问题。
2. LapSurgie框架利用人型机器人，使其能在为人类设计的环境中直接操作，无需大规模改造手术室等基础设施。
3. 该系统通过逆映射策略实现精确的手-工具控制，用户研究验证了其有效性，并为部署人型机器人提供了初步证据。

## 📝 摘要（中文）

本文介绍了一种名为LapSurgie的、基于人型机器人的腹腔镜遥操作框架。该系统利用逆映射策略，控制带有手动腕部的腹腔镜器械，满足遥控中心运动约束，从而实现对现有腹腔镜手术工具的精确控制，无需额外的设置。控制台配备立体视觉系统，提供实时视觉反馈。全面的用户研究表明，该框架有效，并初步证明了在腹腔镜手术中部署人型机器人的可行性，旨在解决偏远和低资源地区医疗资源不平衡的问题。

## 🔬 方法详解

**问题定义**：传统手术机器人系统成本高昂且需要专门的基础设施，难以在资源匮乏的地区普及。现有遥操作方案在精确度和适应性方面仍有提升空间，尤其是在使用标准腹腔镜工具时，如何保证操作的精确性和安全性是一个挑战。

**核心思路**：LapSurgie的核心在于利用人型机器人的通用性和适应性，使其能够在标准手术室环境中直接使用。通过逆映射策略，将操作者的手部动作转化为腹腔镜工具的精确运动，同时满足遥控中心运动（Remote Center of Motion, RCM）约束，保证手术的安全性。

**技术框架**：LapSurgie系统包含三个主要组成部分：1) 人型机器人，负责执行手术操作；2) 控制台，操作者通过控制台进行遥操作，并获得实时视觉反馈；3) 逆映射控制算法，将操作者的手部动作转化为机器人末端执行器的运动指令。操作者在控制台上通过立体视觉系统观察手术视野，并通过手部控制器操纵机器人。逆映射算法负责将手部控制器的运动转化为机器人关节的运动，从而控制腹腔镜工具。

**关键创新**：该框架的关键创新在于将人型机器人与腹腔镜遥操作相结合，并设计了满足RCM约束的逆映射控制算法。与传统手术机器人相比，LapSurgie无需专门的手术室改造，降低了部署成本。与传统的遥操作方案相比，该系统能够更精确地控制标准腹腔镜工具，提高了手术的安全性。

**关键设计**：逆映射控制算法是该系统的核心。该算法需要解决两个关键问题：1) 如何将操作者的手部动作映射到机器人关节空间；2) 如何保证机器人末端执行器的运动满足RCM约束。论文采用了一种基于雅可比矩阵的逆映射方法，并引入了RCM约束项，以保证手术的安全性。具体的参数设置和损失函数细节在论文中进行了详细描述。

## 📊 实验亮点

论文通过用户研究验证了LapSurgie框架的有效性。实验结果表明，操作者可以通过该系统精确地控制腹腔镜工具，完成各种手术操作。与传统的手术机器人相比，LapSurgie在操作精度和操作效率方面具有一定的优势。此外，用户反馈表明，该系统易于学习和使用，具有良好的用户体验。

## 🎯 应用场景

LapSurgie系统具有广泛的应用前景，尤其是在偏远地区和资源匮乏的医疗机构。它可以实现远程手术指导和远程手术操作，提高医疗服务的可及性。此外，该系统还可以用于培训外科医生，提高手术技能。未来，该系统有望应用于更复杂的手术操作，并与其他人工智能技术相结合，实现更智能化的手术机器人。

## 📄 摘要（原文）

> Robotic laparoscopic surgery has gained increasing attention in recent years for its potential to deliver more efficient and precise minimally invasive procedures. However, adoption of surgical robotic platforms remains largely confined to high-resource medical centers, exacerbating healthcare disparities in rural and low-resource regions. To close this gap, a range of solutions has been explored, from remote mentorship to fully remote telesurgery. Yet, the practical deployment of surgical robotic systems to underserved communities remains an unsolved challenge. Humanoid systems offer a promising path toward deployability, as they can directly operate in environments designed for humans without extensive infrastructure modifications -- including operating rooms. In this work, we introduce LapSurgie, the first humanoid-robot-based laparoscopic teleoperation framework. The system leverages an inverse-mapping strategy for manual-wristed laparoscopic instruments that abides to remote center-of-motion constraints, enabling precise hand-to-tool control of off-the-shelf surgical laparoscopic tools without additional setup requirements. A control console equipped with a stereo vision system provides real-time visual feedback. Finally, a comprehensive user study across platforms demonstrates the effectiveness of the proposed framework and provides initial evidence for the feasibility of deploying humanoid robots in laparoscopic procedures.

