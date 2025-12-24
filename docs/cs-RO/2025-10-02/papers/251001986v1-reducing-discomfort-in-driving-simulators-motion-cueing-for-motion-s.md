---
layout: default
title: "Reducing Discomfort in Driving Simulators: Motion Cueing for Motion Sickness Mitigation"
---

# Reducing Discomfort in Driving Simulators: Motion Cueing for Motion Sickness Mitigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01986" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01986v1</a>
  <a href="https://arxiv.org/pdf/2510.01986.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01986v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01986v1', 'Reducing Discomfort in Driving Simulators: Motion Cueing for Motion Sickness Mitigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Varun Kotian, Riender Happee, Barys Shyrokau

**分类**: cs.RO

**发布日期**: 2025-10-02

**备注**: arXiv admin comment: This version has been removed by arXiv administrators as the submitter did not have the rights to agree to the license at the time of submission

---

## 💡 一句话要点

**提出基于MPC的运动提示算法，降低驾驶模拟器中的晕动症**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `驾驶模拟器` `晕动症` `运动提示` `模型预测控制` `主观垂直冲突模型`

## 📋 核心要点

1. 驾驶模拟器易引发晕动症，原因是运动提示的缩放与视觉呈现的不匹配，现有方法难以兼顾模拟的真实感和用户的舒适度。
2. 论文提出基于模型预测控制（MPC）的运动提示算法，通过在代价函数中权衡感觉冲突和比力误差，实现保真度和舒适度的联合优化。
3. 实验结果表明，该算法在不显著降低保真度的情况下，可将晕动症程度降低50%以上，与自适应冲刷算法和纯比力跟踪算法相比有显著提升。

## 📝 摘要（中文）

驾驶模拟器在研发中应用日益广泛。然而，由于运动缩放和未缩放的真实视觉效果，模拟器经常引起晕动症。本文提出了一种运动提示算法，该算法使用模型预测控制（MPC）来降低主观垂直冲突（SVC）模型预测的晕动症。在代价函数中同时惩罚感觉冲突和比力误差，使算法能够联合优化保真度和舒适度。进行了人机环路实验，比较了四种模拟器运动设置：两种基于MPC算法的变体，一种侧重于纯比力跟踪，另一种兼顾比力跟踪和晕动症最小化，以及参考自适应冲刷和无运动情况。实验在一个六自由度驾驶模拟器上进行，参与者接受被动驾驶。

## 🔬 方法详解

**问题定义**：驾驶模拟器中的晕动症问题，源于视觉信息和运动感知之间的冲突。现有运动提示算法难以在保证模拟真实感（比力跟踪）的同时，有效降低晕动症。传统的自适应冲刷算法虽然能减轻晕动症，但会牺牲模拟的真实性。

**核心思路**：论文的核心思路是利用模型预测控制（MPC），在运动提示算法中同时考虑比力跟踪和晕动症最小化。通过在代价函数中同时惩罚比力误差和感觉冲突，实现二者之间的平衡。这种方法允许算法根据驾驶场景和用户状态动态调整运动提示策略，从而在保证一定程度的真实感的同时，显著降低晕动症。

**技术框架**：整体框架包括以下几个主要模块：1) 驾驶场景输入；2) 晕动症模型（SVC模型）预测；3) 基于MPC的运动提示算法，该算法根据驾驶场景和晕动症模型预测结果，生成运动平台的控制信号；4) 六自由度运动平台；5) 用户感知和反馈。MPC算法是核心模块，它接收驾驶场景信息和晕动症模型预测结果，通过优化代价函数，生成运动平台的控制信号。

**关键创新**：最重要的技术创新点在于将晕动症模型（SVC模型）集成到运动提示算法的优化过程中。传统的运动提示算法主要关注比力跟踪，而忽略了晕动症的影响。本文提出的方法通过在代价函数中引入感觉冲突项，实现了对晕动症的直接控制。此外，使用MPC能够预测未来一段时间内的系统状态，从而更好地优化运动提示策略。

**关键设计**：代价函数的设计是关键。代价函数包含两项：比力误差项和感觉冲突项。比力误差项用于衡量运动平台产生的比力与理想比力之间的差异，感觉冲突项用于衡量视觉信息和运动感知之间的冲突程度。两项的权重系数用于调节保真度和舒适度之间的平衡。MPC的预测时域和控制时域需要根据具体的驾驶场景和运动平台动态调整。SVC模型用于预测晕动症程度，其参数需要根据用户的个体差异进行标定。

## 📊 实验亮点

实验结果表明，与自适应冲刷算法和纯比力跟踪算法相比，该算法在不显著降低保真度的情况下，可将晕动症程度降低50%以上（平均MISC等级从3降至1.5）。无运动条件下的晕动症程度最低，但保真度评分也最低。这验证了该算法在保真度和舒适度之间取得良好平衡的能力。

## 🎯 应用场景

该研究成果可应用于各种驾驶模拟器，包括汽车、飞机、船舶等。通过降低晕动症，可以提高驾驶模拟器的可用性和用户体验，使其更广泛地应用于驾驶员培训、车辆研发、人机工程学研究等领域。此外，该方法也可推广到其他类型的运动模拟器，如飞行模拟器、VR游戏等。

## 📄 摘要（原文）

> Driving simulators are increasingly used in research and development. However, simulators often cause motion sickness due to downscaled motion and unscaled veridical visuals. In this paper, a motion cueing algorithm is proposed that reduces motion sickness as predicted by the subjective vertical conflict (SVC) model using model predictive control (MPC). Both sensory conflict and specific force errors are penalised in the cost function, allowing the algorithm to jointly optimise fidelity and comfort.
>   Human-in-the-loop experiments were conducted to compare four simulator motion settings: two variations of our MPC-based algorithm, one focused on pure specific force tracking and the second compromising specific force tracking and motion sickness minimisation, as well as reference adaptive washout and no motion cases. The experiments were performed on a hexapod driving simulator with participants exposed to passive driving.
>   Experimental motion sickness results closely matched the sickness model predictions. As predicted by the model, the no motion condition yielded the lowest sickness levels. However, it was rated lowest in terms of fidelity. The compromise solution reduced sickness by over 50% (average MISC level 3 to 1.5) compared to adaptive washout and the algorithm focusing on specific force tracking, without any significant reduction in fidelity rating.
>   The proposed approach for developing MCA that takes into account both the simulator dynamics and time evolution of motion sickness offers a significant advancement in achieving an optimal control of motion sickness and specific force recreation in driving simulators, supporting broader simulator use.

