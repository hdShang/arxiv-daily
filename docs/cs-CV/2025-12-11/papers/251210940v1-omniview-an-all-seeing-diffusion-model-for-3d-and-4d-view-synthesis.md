---
layout: default
title: OmniView: An All-Seeing Diffusion Model for 3D and 4D View Synthesis
---

# OmniView: An All-Seeing Diffusion Model for 3D and 4D View Synthesis

**arXiv**: [2512.10940v1](https://arxiv.org/abs/2512.10940) | [PDF](https://arxiv.org/pdf/2512.10940.pdf)

**作者**: Xiang Fan, Sharath Girish, Vivek Ramanujan, Chaoyang Wang, Ashkan Mirzaei, Petr Sushko, Aliaksandr Siarohin, Sergey Tulyakov, Ranjay Krishna

---

## 💡 一句话要点

**提出OmniView统一框架，通过分离空间、时间和视角条件实现多任务4D一致性合成。**

**关键词**: `4D一致性合成` `扩散模型` `视角合成` `相机控制` `统一框架`

## 📋 核心要点

1. 核心问题：现有方法在4D一致性任务中分散，缺乏统一模型处理多种输入组合。
2. 方法要点：独立表示空间、时间和视角条件，支持灵活组合以泛化至静态、动态和多视角合成。
3. 实验或效果：在多个基准上优于任务特定模型，提升图像质量分数并减少相机轨迹误差。

## 📄 摘要（原文）

> Prior approaches injecting camera control into diffusion models have focused on specific subsets of 4D consistency tasks: novel view synthesis, text-to-video with camera control, image-to-video, amongst others. Therefore, these fragmented approaches are trained on disjoint slices of available 3D/4D data. We introduce OmniView, a unified framework that generalizes across a wide range of 4D consistency tasks. Our method separately represents space, time, and view conditions, enabling flexible combinations of these inputs. For example, OmniView can synthesize novel views from static, dynamic, and multiview inputs, extrapolate trajectories forward and backward in time, and create videos from text or image prompts with full camera control. OmniView is competitive with task-specific models across diverse benchmarks and metrics, improving image quality scores among camera-conditioned diffusion models by up to 33\% in multiview NVS LLFF dataset, 60\% in dynamic NVS Neural 3D Video benchmark, 20\% in static camera control on RE-10K, and reducing camera trajectory errors by 4x in text-conditioned video generation. With strong generalizability in one model, OmniView demonstrates the feasibility of a generalist 4D video model. Project page is available at https://snap-research.github.io/OmniView/

