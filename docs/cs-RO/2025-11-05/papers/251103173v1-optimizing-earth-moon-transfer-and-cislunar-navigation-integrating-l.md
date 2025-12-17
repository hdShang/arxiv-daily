---
layout: default
title: Optimizing Earth-Moon Transfer and Cislunar Navigation: Integrating Low-Energy Trajectories, AI Techniques and GNSS-R Technologies
---

# Optimizing Earth-Moon Transfer and Cislunar Navigation: Integrating Low-Energy Trajectories, AI Techniques and GNSS-R Technologies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03173" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03173v1</a>
  <a href="https://arxiv.org/pdf/2511.03173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03173v1" onclick="toggleFavorite(this, '2511.03173v1', 'Optimizing Earth-Moon Transfer and Cislunar Navigation: Integrating Low-Energy Trajectories, AI Techniques and GNSS-R Technologies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arsalan Muhammad, Wasiu Akande Ahmed, Omada Friday Ojonugwa, Paul Puspendu Biswas

**分类**: astro-ph.EP, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-11-05

**期刊**: Published in the Proceedings of 2nd IAASPAICE 2025

---

## 💡 一句话要点

**融合低能轨道、AI与GNSS-R技术，优化地月转移和月球导航**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `地月转移` `环月导航` `人工智能` `GNSS-R` `低能轨道` `深度强化学习` `卷积神经网络`

## 📋 核心要点

1. 传统地月转移对发射窗口要求苛刻，推进剂消耗大，且地球GNSS系统在环月空间覆盖不足，限制了自主性和环境感知。
2. 该研究融合低能轨道设计、人工智能技术（CNN、DRL）和GNSS-R技术，旨在优化地月转移和环月导航。
3. 通过AI进行地形识别和轨道优化，并利用GNSS-R扩展导航能力，为可持续的环月探索提供可扩展的框架。

## 📝 摘要（中文）

日益增长的环月活动，包括登月、月球门户以及在轨燃料补给站，需要经济高效的轨道设计以及可靠的导航和遥感集成。传统的地月转移存在发射窗口固定和推进剂需求高等问题，而地球GNSS系统几乎无法覆盖地球同步轨道以外的区域，限制了环月空间的自主性和环境感知能力。本文综述了四种主要的转移策略，评估了速度需求、飞行时间和燃料效率，并确定了它们对载人任务和机器人任务的适用性。重点介绍了人工智能和机器学习的新兴作用：卷积神经网络支持自动陨石坑识别和数字地形模型生成，而深度强化学习支持下降和着陆期间的自适应轨道优化，以降低风险和决策延迟。该研究还探讨了GNSS反射测量和先进的定位、导航和授时架构如何扩展导航能力。GNSS-R可以作为双基地雷达，用于绘制月球冰、土壤特性和表面地形图，而PNT系统支持自主交会、拉格朗日点驻留和协调卫星群操作。这些发展结合起来，为可持续的环月探索和人类及机器人的长期存在建立了一个可扩展的框架。

## 🔬 方法详解

**问题定义**：论文旨在解决传统地月转移任务中存在的推进剂需求高、发射窗口受限以及环月空间导航能力不足的问题。现有方法依赖于固定的轨道设计和地球基站的辅助，难以满足未来大规模环月活动的需求，尤其是在自主性和环境感知方面存在瓶颈。

**核心思路**：论文的核心思路是整合多种先进技术，包括低能转移轨道设计、人工智能算法和GNSS-R技术，以实现更经济、更自主和更可靠的地月转移和环月导航。通过优化轨道设计降低推进剂消耗，利用AI增强环境感知和决策能力，并扩展导航系统的覆盖范围。

**技术框架**：整体框架包括三个主要部分：1) **轨道设计优化**：比较和选择适合不同任务类型的低能转移轨道；2) **AI驱动的导航与感知**：利用卷积神经网络进行月球表面特征识别，利用深度强化学习进行着陆过程中的轨道优化；3) **GNSS-R增强导航**：利用GNSS反射信号进行月球表面测绘和扩展导航覆盖范围。这些部分相互协同，共同提升地月转移和环月导航的性能。

**关键创新**：论文的关键创新在于将人工智能技术（特别是CNN和DRL）与传统的轨道设计和导航技术相结合，实现更智能、更自主的环月任务。此外，利用GNSS-R技术扩展导航覆盖范围也是一个重要的创新点，克服了传统GNSS系统在环月空间的局限性。

**关键设计**：在AI方面，CNN被用于自动识别月球表面的陨石坑，为导航提供关键的地标信息。DRL则被用于优化着陆过程中的轨道，通过学习最优策略来降低风险和决策延迟。在GNSS-R方面，通过分析反射信号的特性来推断月球表面的土壤性质和地形信息。具体的参数设置、损失函数和网络结构等细节在论文中可能未详细给出，属于未来的研究方向。

## 📊 实验亮点

论文综述了多种地月转移策略，并强调了AI和GNSS-R在提升环月导航能力方面的潜力。虽然没有提供具体的实验数据，但明确指出了CNN在陨石坑识别和DRL在轨道优化中的应用方向，为未来的研究提供了清晰的路线图。GNSS-R作为双基地雷达用于月球表面测绘的设想也具有重要的应用前景。

## 🎯 应用场景

该研究成果可应用于未来的月球探测任务、月球基地建设、空间资源开发以及深空探索等领域。通过降低地月转移的成本和提高环月导航的自主性，可以促进更大规模、更可持续的环月活动，并为未来的载人登月和深空探索提供技术支持。

## 📄 摘要（原文）

> The rapid growth of cislunar activities, including lunar landings, the Lunar Gateway, and in-space refueling stations, requires advances in cost-efficient trajectory design and reliable integration of navigation and remote sensing. Traditional Earth-Moon transfers suffer from rigid launch windows and high propellant demands, while Earth-based GNSS systems provide little to no coverage beyond geostationary orbit. This limits autonomy and environmental awareness in cislunar space. This review compares four major transfer strategies by evaluating velocity requirements, flight durations, and fuel efficiency, and by identifying their suitability for both crewed and robotic missions. The emerging role of artificial intelligence and machine learning is highlighted: convolutional neural networks support automated crater recognition and digital terrain model generation, while deep reinforcement learning enables adaptive trajectory refinement during descent and landing to reduce risk and decision latency. The study also examines how GNSS-Reflectometry and advanced Positioning, Navigation, and Timing architectures can extend navigation capabilities beyond current limits. GNSS-R can act as a bistatic radar for mapping lunar ice, soil properties, and surface topography, while PNT systems support autonomous rendezvous, Lagrange point station-keeping, and coordinated satellite swarm operations. Combining these developments establishes a scalable framework for sustainable cislunar exploration and long-term human and robotic presence.

