---
layout: default
title: "Swarm-GPT: Combining Large Language Models with Safe Motion Planning for Robot Choreography Design"
---

# Swarm-GPT: Combining Large Language Models with Safe Motion Planning for Robot Choreography Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.01059" class="toolbar-btn" target="_blank">📄 arXiv: 2312.01059v1</a>
  <a href="https://arxiv.org/pdf/2312.01059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.01059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.01059v1', 'Swarm-GPT: Combining Large Language Models with Safe Motion Planning for Robot Choreography Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aoran Jiao, Tanmay P. Patel, Sanjmi Khurana, Anna-Mariya Korol, Lukas Brunke, Vivek K. Adajania, Utku Culha, Siqi Zhou, Angela P. Schoellig

**分类**: cs.RO

**发布日期**: 2023-12-02

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**Swarm-GPT：结合LLM与安全运动规划的无人机群舞自动设计系统**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机群舞` `大型语言模型` `运动规划` `自动化设计` `人机协作`

## 📋 核心要点

1. 现有无人机群舞设计缺乏自动化，依赖人工设计，难以保证安全性和创造性。
2. Swarm-GPT利用LLM生成创意航点，结合安全运动规划算法，实现无人机群舞的自动生成。
3. 实验表明，Swarm-GPT能有效迁移到真实环境，并在实际活动中安全部署，平均RMSE为28.7mm。

## 📝 摘要（中文）

本文提出Swarm-GPT，一个将大型语言模型（LLM）与安全集群运动规划相结合的系统，为可部署的无人机群舞提供了一种自动化和新颖的方法。Swarm-GPT使用户能够通过自然语言指令自动生成同步的无人机表演。Swarm-GPT强调安全性和创造性，通过将生成模型的创造力与基于模型的规划算法的有效性和安全性相结合，弥补了无人机群舞领域的关键空白。该目标通过提示LLM基于提取的音频数据生成一组独特的航点来实现。轨迹规划器处理这些航点，以保证无碰撞和可行的运动。结果可以在执行前在模拟中查看，并通过动态重新提示进行修改。从仿真到真实的迁移实验表明，Swarm-GPT能够准确地复制模拟的无人机轨迹，平均仿真到真实的均方根误差（RMSE）为28.7毫米。迄今为止，Swarm-GPT已在三个现场活动中成功展示，体现了预训练模型的安全实际部署。

## 🔬 方法详解

**问题定义**：无人机群舞的设计通常需要人工干预，耗时且难以保证安全性和创造性。现有的方法可能无法充分利用生成模型的创造力，也难以确保运动规划的安全性，尤其是在真实环境中部署时。

**核心思路**：Swarm-GPT的核心思路是将大型语言模型的创造性能力与基于模型的运动规划算法的安全性相结合。通过LLM生成富有创意的航点，然后利用运动规划算法确保无人机群体的安全飞行，从而实现自动化、安全且具有艺术性的无人机群舞设计。

**技术框架**：Swarm-GPT的整体框架包含以下几个主要模块：1) 音频数据提取：从音频输入中提取相关特征。2) LLM提示：利用提取的音频特征提示LLM生成无人机群舞的航点。3) 轨迹规划：使用轨迹规划器处理LLM生成的航点，生成无碰撞且可行的无人机轨迹。4) 仿真验证：在仿真环境中验证生成的轨迹，并进行动态重新提示以优化效果。5) 真实部署：将仿真验证后的轨迹部署到真实的无人机群中。

**关键创新**：Swarm-GPT的关键创新在于将LLM的生成能力与传统的运动规划算法相结合，实现无人机群舞的自动化设计。与传统方法相比，Swarm-GPT能够自动生成更具创意和艺术性的无人机群舞，同时保证安全性。

**关键设计**：在LLM提示方面，论文可能使用了特定的提示工程技术，以确保LLM能够生成符合要求的航点。在轨迹规划方面，可能采用了考虑无人机动力学约束和碰撞避免的优化算法。具体的参数设置和损失函数等技术细节在论文中可能有所描述，但此处未知。

## 📊 实验亮点

Swarm-GPT在仿真和真实环境中的实验结果均表现出色。仿真结果表明，该系统能够生成安全且具有创意的无人机群舞轨迹。从仿真到真实的迁移实验表明，Swarm-GPT能够准确地复制模拟的无人机轨迹，平均仿真到真实的均方根误差（RMSE）为28.7毫米。Swarm-GPT已在三个现场活动中成功展示，验证了其在真实环境中的可行性和安全性。

## 🎯 应用场景

Swarm-GPT可应用于各种需要无人机群舞表演的场景，例如大型活动、音乐会、体育赛事和节日庆典等。该系统能够降低无人机群舞设计的门槛，使得更多人能够轻松创作出精彩的无人机表演。此外，Swarm-GPT还可用于教育和研究领域，促进无人机群舞技术的创新和发展。

## 📄 摘要（原文）

> This paper presents Swarm-GPT, a system that integrates large language models (LLMs) with safe swarm motion planning - offering an automated and novel approach to deployable drone swarm choreography. Swarm-GPT enables users to automatically generate synchronized drone performances through natural language instructions. With an emphasis on safety and creativity, Swarm-GPT addresses a critical gap in the field of drone choreography by integrating the creative power of generative models with the effectiveness and safety of model-based planning algorithms. This goal is achieved by prompting the LLM to generate a unique set of waypoints based on extracted audio data. A trajectory planner processes these waypoints to guarantee collision-free and feasible motion. Results can be viewed in simulation prior to execution and modified through dynamic re-prompting. Sim-to-real transfer experiments demonstrate Swarm-GPT's ability to accurately replicate simulated drone trajectories, with a mean sim-to-real root mean square error (RMSE) of 28.7 mm. To date, Swarm-GPT has been successfully showcased at three live events, exemplifying safe real-world deployment of pre-trained models.

