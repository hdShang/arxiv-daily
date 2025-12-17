---
layout: default
title: ShowTable: Unlocking Creative Table Visualization with Collaborative Reflection and Refinement
---

# ShowTable: Unlocking Creative Table Visualization with Collaborative Reflection and Refinement

**arXiv**: [2512.13303v1](https://arxiv.org/abs/2512.13303) | [PDF](https://arxiv.org/pdf/2512.13303.pdf)

**作者**: Zhihang Liu, Xiaoyi Bao, Pandeng Li, Junjie Zhou, Zhaohe Liao, Yefei He, Kaixun Jiang, Chen-Wei Xie, Yun Zheng, Hongtao Xie

---

## 💡 一句话要点

**提出ShowTable管道，通过协作反思与精炼解决创意表格可视化任务**

**关键词**: `创意表格可视化` `多模态大语言模型` `扩散模型` `协作反思` `数据构造管道` `基准评估`

## 📋 核心要点

1. 核心问题：现有模型在需要深度推理和精确数据映射的创意表格可视化任务上表现不足
2. 方法要点：结合MLLM作为中央协调器进行推理和错误校正，扩散模型执行指令，实现高保真生成
3. 实验或效果：在TableVisBench基准上显著优于基线，验证了多模态推理和错误校正能力

## 📄 摘要（原文）

> While existing generation and unified models excel at general image generation, they struggle with tasks requiring deep reasoning, planning, and precise data-to-visual mapping abilities beyond general scenarios. To push beyond the existing limitations, we introduce a new and challenging task: creative table visualization, requiring the model to generate an infographic that faithfully and aesthetically visualizes the data from a given table. To address this challenge, we propose ShowTable, a pipeline that synergizes MLLMs with diffusion models via a progressive self-correcting process. The MLLM acts as the central orchestrator for reasoning the visual plan and judging visual errors to provide refined instructions, the diffusion execute the commands from MLLM, achieving high-fidelity results. To support this task and our pipeline, we introduce three automated data construction pipelines for training different modules. Furthermore, we introduce TableVisBench, a new benchmark with 800 challenging instances across 5 evaluation dimensions, to assess performance on this task. Experiments demonstrate that our pipeline, instantiated with different models, significantly outperforms baselines, highlighting its effective multi-modal reasoning, generation, and error correction capabilities.

