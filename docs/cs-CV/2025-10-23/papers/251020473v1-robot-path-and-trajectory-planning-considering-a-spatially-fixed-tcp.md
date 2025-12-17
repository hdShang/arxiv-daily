---
layout: default
title: Robot Path and Trajectory Planning Considering a Spatially Fixed TCP
---

# Robot Path and Trajectory Planning Considering a Spatially Fixed TCP

**arXiv**: [2510.20473v1](https://arxiv.org/abs/2510.20473) | [PDF](https://arxiv.org/pdf/2510.20473.pdf)

**作者**: Bernhard Rameder, Hubert Gattringer, Andreas Mueller, Ronald Naderer

---

## 💡 一句话要点

**提出基于空间固定TCP的机器人轨迹规划方法，以简化工件移动场景**

**关键词**: `机器人轨迹规划` `空间固定TCP` `B样条路径` `工件移动优化` `工业机器人验证`

## 📋 核心要点

1. 核心问题：在工件移动场景中规划机器人轨迹，需考虑加工路径和TCP固定约束
2. 方法要点：使用B样条表示路径，确保连续性和平滑轨迹，结合预设方向和TCP速度
3. 实验或效果：在工业机器人上验证，处理任意定义工件，实现平滑轨迹

## 📄 摘要（原文）

> This paper presents a method for planning a trajectory in workspace
> coordinates using a spatially fixed tool center point (TCP), while taking into
> account the processing path on a part. This approach is beneficial if it is
> easier to move the part rather than moving the tool. Whether a mathematical
> description that defines the shape to be processed or single points from a
> design program are used, the robot path is finally represented using B-splines.
> The use of splines enables the path to be continuous with a desired degree,
> which finally leads to a smooth robot trajectory. While calculating the robot
> trajectory through prescribed orientation, additionally a given velocity at the
> TCP has to be considered. The procedure was validated on a real system using an
> industrial robot moving an arbitrary defined part.

